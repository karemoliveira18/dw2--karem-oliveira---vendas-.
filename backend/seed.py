from sqlalchemy.orm import Session
from .database import engine, SessionLocal, Base
from .models import Produto

# Cria tabelas
Base.metadata.create_all(bind=engine)
db: Session = SessionLocal()

produtos = [
    {"nome": "Camiseta Rosa", "descricao": "Camiseta estilosa rosa claro", "preco": 59.90, "estoque": 10, "categoria": "Roupas", "sku": "CAM001"},
    {"nome": "Tênis Branco", "descricao": "Tênis esportivo confortável", "preco": 199.90, "estoque": 5, "categoria": "Calçados", "sku": "TEN002"},
    {"nome": "Bolsa Feminina", "descricao": "Bolsa com alça longa", "preco": 149.90, "estoque": 8, "categoria": "Acessórios", "sku": "BOL003"},
    {"nome": "Boné Azul", "descricao": "Boné unissex casual", "preco": 39.90, "estoque": 15, "categoria": "Acessórios", "sku": "BON004"},
    {"nome": "Jaqueta Jeans", "descricao": "Jaqueta clássica jeans", "preco": 249.90, "estoque": 6, "categoria": "Roupas", "sku": "JAC005"},
    {"nome": "Mochila Escolar", "descricao": "Mochila grande, resistente", "preco": 129.90, "estoque": 12, "categoria": "Acessórios", "sku": "MOC006"},
    {"nome": "Calça Legging", "descricao": "Calça confortável preta", "preco": 79.90, "estoque": 20, "categoria": "Roupas", "sku": "CAL007"},
    {"nome": "Meias Coloridas", "descricao": "Kit com 5 pares", "preco": 29.90, "estoque": 30, "categoria": "Roupas", "sku": "MES008"},
    {"nome": "Tênis Infantil", "descricao": "Tênis esportivo para crianças", "preco": 159.90, "estoque": 7, "categoria": "Calçados", "sku": "TEN009"},
    {"nome": "Relógio Digital", "descricao": "Relógio com cronômetro", "preco": 99.90, "estoque": 10, "categoria": "Acessórios", "sku": "REL010"},
    {"nome": "Camiseta Branca", "descricao": "Camiseta básica branca", "preco": 49.90, "estoque": 25, "categoria": "Roupas", "sku": "CAM011"},
    {"nome": "Sandália Feminina", "descricao": "Sandália confortável", "preco": 89.90, "estoque": 14, "categoria": "Calçados", "sku": "SAN012"},
    {"nome": "Blusa Moletom", "descricao": "Moletom quentinho cinza", "preco": 119.90, "estoque": 10, "categoria": "Roupas", "sku": "BLO013"},
    {"nome": "Óculos de Sol", "descricao": "Óculos estilo aviador", "preco": 79.90, "estoque": 18, "categoria": "Acessórios", "sku": "OCU014"},
    {"nome": "Tênis Esportivo", "descricao": "Para corrida e academia", "preco": 209.90, "estoque": 9, "categoria": "Calçados", "sku": "TEN015"},
    {"nome": "Saia Plissada", "descricao": "Saia leve feminina", "preco": 99.90, "estoque": 11, "categoria": "Roupas", "sku": "SAI016"},
    {"nome": "Carteira Masculina", "descricao": "Carteira de couro marrom", "preco": 59.90, "estoque": 20, "categoria": "Acessórios", "sku": "CAR017"},
    {"nome": "Chinelo Unissex", "descricao": "Chinelo confortável", "preco": 29.90, "estoque": 30, "categoria": "Calçados", "sku": "CHI018"},
    {"nome": "Jaqueta Corta-Vento", "descricao": "Jaqueta leve para esportes", "preco": 179.90, "estoque": 8, "categoria": "Roupas", "sku": "JAC019"},
    {"nome": "Bolsa de Ombro", "descricao": "Bolsa pequena feminina", "preco": 129.90, "estoque": 10, "categoria": "Acessórios", "sku": "BOL020"}
]

for p in produtos:
    produto = Produto(**p)
    db.add(produto)

db.commit()
db.close()
print("✅ 20 produtos inseridos no SQLite com sucesso!")
