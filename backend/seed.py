from .database import SessionLocal, init_db
from .models import Produto


def seed():
    init_db()
    db = SessionLocal()
    produtos = [
        {"nome": "Tênis Runner Azul", "descricao": "Tênis esportivo com amortecimento e solado aderente, ideal para corrida e uso diário.", "image_url": "https://images.unsplash.com/photo-1519744792095-2f2205e87b6f?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=1", "preco": 199.90, "estoque": 10, "categoria": "Calçados", "sku": "TRB-001"},
        {"nome": "Camiseta Esportiva", "descricao": "Camiseta dry-fit de alta respirabilidade, ótima para treinos e uso casual.", "image_url": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=2", "preco": 49.90, "estoque": 30, "categoria": "Roupas", "sku": "CE-002"},
        {"nome": "Mochila Escolar", "descricao": "Resistente e espaçosa", "preco": 129.90, "estoque": 15, "categoria": "Acessórios", "sku": "ME-003"},
        {"nome": "Mochila Escolar", "descricao": "Mochila com compartimento para notebook, alças acolchoadas e múltiplos bolsos.", "image_url": "https://images.unsplash.com/photo-1520975919200-1e3b0fb6f3b7?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=3", "preco": 129.90, "estoque": 15, "categoria": "Acessórios", "sku": "ME-003"},
        {"nome": "Garrafa Squeeze", "descricao": "Garrafa inox 500ml com isolamento térmico e tampa vedante.", "image_url": "https://images.unsplash.com/photo-1526401281623-58a03b2f093c?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=4", "preco": 39.90, "estoque": 50, "categoria": "Acessórios", "sku": "GS-004"},
        {"nome": "Boné Snapback", "descricao": "Ajustável", "preco": 59.90, "estoque": 20, "categoria": "Acessórios", "sku": "BS-005"},
        {"nome": "Boné Snapback", "descricao": "Boné ajustável com aba reta, tecido respirável e costura reforçada.", "image_url": "https://images.unsplash.com/photo-1512436991641-6745cdb1723f?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=5", "preco": 59.90, "estoque": 20, "categoria": "Acessórios", "sku": "BS-005"},
        {"nome": "Jaqueta Corta-Vento", "descricao": "Jaqueta leve com forro interno, ideal para trilhas e dias ventosos.", "image_url": "https://images.unsplash.com/photo-1549399543-4f4b6f0a0b8c?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=6", "preco": 179.90, "estoque": 8, "categoria": "Roupas", "sku": "JC-006"},
        {"nome": "Meias Pack 3", "descricao": "Conforto diário", "preco": 29.90, "estoque": 100, "categoria": "Roupas", "sku": "MP3-007"},
        {"nome": "Meias Pack 3", "descricao": "Pack com 3 pares de meias confortáveis e duráveis.", "image_url": "https://images.unsplash.com/photo-1520975919200-1e3b0fb6f3b7?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=7", "preco": 29.90, "estoque": 100, "categoria": "Roupas", "sku": "MP3-007"},
        {"nome": "Agenda 2026", "descricao": "Agenda com capa dura, planejamento mensal e notas.", "image_url": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=8", "preco": 24.90, "estoque": 45, "categoria": "Papelaria", "sku": "AG-008"},
        {"nome": "Caderno Universitário", "descricao": "200 folhas", "preco": 12.90, "estoque": 200, "categoria": "Papelaria", "sku": "CU-009"},
        {"nome": "Caderno Universitário", "descricao": "Caderno 200 folhas com capa plástica resistente.", "image_url": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=9", "preco": 12.90, "estoque": 200, "categoria": "Papelaria", "sku": "CU-009"},
        {"nome": "Lápis HB - 12un", "descricao": "Lápis HB de grafite de alta qualidade, embalagem com 12 unidades.", "image_url": "https://images.unsplash.com/photo-1526318472351-c75fcf070ae5?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=10", "preco": 9.90, "estoque": 300, "categoria": "Papelaria", "sku": "LP-010"},
        {"nome": "Caneta Gel", "descricao": "Escrita suave", "preco": 4.90, "estoque": 500, "categoria": "Papelaria", "sku": "CG-011"},
        {"nome": "Caneta Gel", "descricao": "Caneta gel com ponta 0.7mm e tinta resistente à água.", "image_url": "https://images.unsplash.com/photo-1520975919200-1e3b0fb6f3b7?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=11", "preco": 4.90, "estoque": 500, "categoria": "Papelaria", "sku": "CG-011"},
        {"nome": "Estojo Multiuso", "descricao": "Estojo em tecido resistente com zíper e bolsos internos.", "image_url": "https://images.unsplash.com/photo-1598300050616-7b8b4d8f6a1a?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=12", "preco": 34.90, "estoque": 60, "categoria": "Acessórios", "sku": "EM-012"},
        {"nome": "Tênis Casual Branco", "descricao": "Estilo urbano", "preco": 149.90, "estoque": 12, "categoria": "Calçados", "sku": "TCB-013"},
        {"nome": "Tênis Casual Branco", "descricao": "Tênis casual com solado emborrachado e acabamento em material sintético.", "image_url": "https://images.unsplash.com/photo-1519744792095-2f2205e87b6f?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=13", "preco": 149.90, "estoque": 12, "categoria": "Calçados", "sku": "TCB-013"},
        {"nome": "Bolsa Transversal", "descricao": "Bolsa compacta com alça ajustável e bolso externo.", "image_url": "https://images.unsplash.com/photo-1520975919200-1e3b0fb6f3b7?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=14", "preco": 89.90, "estoque": 25, "categoria": "Acessórios", "sku": "BT-014"},
        {"nome": "Relógio Digital", "descricao": "Resistente à água", "preco": 79.90, "estoque": 40, "categoria": "Acessórios", "sku": "RD-015"},
        {"nome": "Relógio Digital", "descricao": "Relógio digital com cronômetro e resistência à água.", "image_url": "https://images.unsplash.com/photo-1519744792095-2f2205e87b6f?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=15", "preco": 79.90, "estoque": 40, "categoria": "Acessórios", "sku": "RD-015"},
        {"nome": "Fone de Ouvido", "descricao": "Fone estéreo com cabo de 1.2m, confortável para uso diário.", "image_url": "https://images.unsplash.com/photo-1512314889357-e157c22f938d?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=16", "preco": 59.90, "estoque": 35, "categoria": "Eletrônicos", "sku": "FO-016"},
        {"nome": "Mouse Óptico", "descricao": "USB, 1600 DPI", "preco": 49.90, "estoque": 80, "categoria": "Eletrônicos", "sku": "MO-017"},
        {"nome": "Mouse Óptico", "descricao": "Mouse USB com sensor óptico 1600 DPI e design ergonômico.", "image_url": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=17", "preco": 49.90, "estoque": 80, "categoria": "Eletrônicos", "sku": "MO-017"},
        {"nome": "Teclado Slim", "descricao": "Teclado slim USB com teclas de baixo perfil.", "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=18", "preco": 69.90, "estoque": 40, "categoria": "Eletrônicos", "sku": "TS-018"},
        {"nome": "Capa para Notebook", "descricao": "Neoprene 15''", "preco": 99.90, "estoque": 22, "categoria": "Acessórios", "sku": "CN-019"},
        {"nome": "Capa para Notebook", "descricao": "Capa em neoprene 15'' com proteção contra arranhões.", "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=19", "preco": 99.90, "estoque": 22, "categoria": "Acessórios", "sku": "CN-019"},
        {"nome": "Chinelo Slide", "descricao": "Chinelo confortável com sola antiderrapante.", "image_url": "https://images.unsplash.com/photo-1503341455253-b2e723bb3dbb?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=20", "preco": 29.90, "estoque": 70, "categoria": "Calçados", "sku": "CS-020"},
    ]

    for p in produtos:
        existing = db.query(Produto).filter(Produto.nome == p["nome"]).first()
        if not existing:
            prod = Produto(**p)
            db.add(prod)
    db.commit()
    db.close()


if __name__ == "__main__":
    seed()
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
