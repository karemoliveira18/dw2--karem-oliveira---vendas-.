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
