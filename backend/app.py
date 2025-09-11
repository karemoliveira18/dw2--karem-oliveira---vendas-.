from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, database
from pydantic import BaseModel, Field, validator
from typing import Optional, List


app = FastAPI(title="Loja Escolar API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ProdutoCreate(BaseModel):
    nome: str = Field(..., min_length=3, max_length=60)
    descricao: Optional[str] = None
    image_url: Optional[str] = None
    preco: float = Field(..., gt=0)
    estoque: int = Field(0, ge=0)
    categoria: Optional[str] = None
    sku: Optional[str] = None

    @validator('image_url')
    def validate_image_url(cls, v):
        if v and len(v) > 300:
            raise ValueError('image_url muito longa')
        return v


class ProdutoOut(ProdutoCreate):
    id: int

    class Config:
        orm_mode = True


@app.on_event("startup")
def startup():
    database.init_db()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/produtos", response_model=List[ProdutoOut])
def listar_produtos(search: Optional[str] = None, categoria: Optional[str] = None, sort: Optional[str] = None, db: Session = Depends(get_db)):
    q = db.query(models.Produto)
    if search:
        q = q.filter(models.Produto.nome.ilike(f"%{search}%"))
    if categoria:
        q = q.filter(models.Produto.categoria == categoria)
    if sort == "preco_asc":
        q = q.order_by(models.Produto.preco.asc())
    elif sort == "preco_desc":
        q = q.order_by(models.Produto.preco.desc())
    elif sort == "nome_asc":
        q = q.order_by(models.Produto.nome.asc())
    return q.all()


@app.get("/produtos/{produto_id}", response_model=ProdutoOut)
def get_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(models.Produto).get(produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@app.post("/produtos", response_model=ProdutoOut, status_code=201)
def criar_produto(p: ProdutoCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Produto).filter(models.Produto.nome == p.nome).first()
    if existing:
        raise HTTPException(status_code=400, detail="Produto com esse nome já existe")
    produto = models.Produto(**p.dict())
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto


@app.put("/produtos/{produto_id}", response_model=ProdutoOut)
def atualizar_produto(produto_id: int, p: ProdutoCreate, db: Session = Depends(get_db)):
    produto = db.query(models.Produto).get(produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    for field, value in p.dict().items():
        setattr(produto, field, value)
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto


@app.delete("/produtos/{produto_id}")
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(models.Produto).get(produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db.delete(produto)
    db.commit()
    return {"detail": "Produto removido"}


class ItemPedido(BaseModel):
    produto_id: int
    quantidade: int = Field(..., ge=1)


class CarrinhoConfirm(BaseModel):
    itens: List[ItemPedido]
    cupom: Optional[str] = None


@app.post("/carrinho/confirmar")
def confirmar_carrinho(body: CarrinhoConfirm, db: Session = Depends(get_db)):
    total = 0.0
    produtos_update = []
    for item in body.itens:
        produto = db.query(models.Produto).get(item.produto_id)
        if not produto:
            raise HTTPException(status_code=404, detail=f"Produto {item.produto_id} não encontrado")
        if produto.estoque < item.quantidade:
            raise HTTPException(status_code=400, detail=f"Estoque insuficiente para {produto.nome}")
        total += produto.preco * item.quantidade
        produtos_update.append((produto, item.quantidade))

    desconto = 0.0
    if body.cupom and body.cupom.upper() == "ALUNO10":
        desconto = total * 0.10

    total_final = float(total - desconto)

    for produto, qtd in produtos_update:
        produto.estoque = produto.estoque - qtd
        db.add(produto)

    pedido = models.Pedido(total_final=total_final)
    db.add(pedido)
    db.commit()
    return {"pedido_id": pedido.id, "total_final": total_final}

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .models import Produto
from datetime import datetime

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# exemplo GET produtos
@app.get("/produtos")
def get_produtos(search: str = "", categoria: str = "", sort: str = ""):
    db = next(get_db())
    query = db.query(Produto)
    if search:
        query = query.filter(Produto.nome.contains(search))
    if categoria:
        query = query.filter(Produto.categoria == categoria)
    if sort == "preco":
        query = query.order_by(Produto.preco)
    return query.all()
