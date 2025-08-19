from app import app, db, Produto

with app.app_context():
    db.create_all()
    
    produtos = [
        Produto(nome='Caderno Universitário', descricao='Capa dura, 200 folhas', preco=24.90, estoque=50, categoria='Papelaria', sku='CAD001'),
        Produto(nome='Caneta Esferográfica Azul', descricao='Ponta fina, tinta azul', preco=2.50, estoque=200, categoria='Papelaria', sku='CAN002'),
        Produto(nome='Lápis de Cor 12 cores', descricao='Estojo com 12 cores', preco=15.90, estoque=80, categoria='Papelaria', sku='LAP003'),
        Produto(nome='Mochila Escolar', descricao='Mochila resistente, vários bolsos', preco=89.90, estoque=30, categoria='Acessórios', sku='MOC004'),
        Produto(nome='Borracha Branca', descricao='Borracha macia', preco=1.80, estoque=150, categoria='Papelaria', sku='BOR005'),
        # ... outros produtos ...
    ]
    db.session.bulk_save_objects(produtos)
    db.session.commit()

if __name__ == '__main__':
    db.session.bulk_save_objects(produtos)
    db.session.commit()
    print("Banco de dados criado e produtos inseridos com sucesso!")

def seed():
    produtos = [
        Produto(nome='Caderno Universitário', descricao='Capa dura, 200 folhas', preco=24.90, estoque=50, categoria='Papelaria', sku='CAD001'),
        Produto(nome='Caneta Esferográfica Azul', descricao='Ponta fina, tinta azul', preco=2.50, estoque=200, categoria='Papelaria', sku='CAN002'),
        Produto(nome='Lápis de Cor 12 cores', descricao='Estojo com 12 cores', preco=15.90, estoque=80, categoria='Papelaria', sku='LAP003'),
        Produto(nome='Mochila Escolar', descricao='Mochila resistente, vários bolsos', preco=89.90, estoque=30, categoria='Acessórios', sku='MOC004'),
        Produto(nome='Borracha Branca', descricao='Borracha macia', preco=1.80, estoque=150, categoria='Papelaria', sku='BOR005'),
        Produto(nome='Apontador Duplo', descricao='Com depósito', preco=3.20, estoque=100, categoria='Papelaria', sku='APP006'),
        Produto(nome='Marca Texto Amarelo', descricao='Cor vibrante', preco=4.50, estoque=60, categoria='Papelaria', sku='MAR007'),
        Produto(nome='Estojo Escolar', descricao='Estojo grande, zíper reforçado', preco=19.90, estoque=40, categoria='Acessórios', sku='EST008'),
        Produto(nome='Agenda 2025', descricao='Agenda diária, capa personalizada', preco=29.90, estoque=25, categoria='Papelaria', sku='AGE009'),
        Produto(nome='Calculadora Científica', descricao='Funções avançadas', preco=59.90, estoque=20, categoria='Eletrônicos', sku='CAL010'),
        Produto(nome='Régua 30cm', descricao='Plástico transparente', preco=2.90, estoque=90, categoria='Papelaria', sku='REG011'),
        Produto(nome='Cola Branca 90g', descricao='Não tóxica', preco=5.50, estoque=70, categoria='Papelaria', sku='COL012'),
        Produto(nome='Tesoura Escolar', descricao='Ponta arredondada', preco=7.90, estoque=60, categoria='Acessórios', sku='TES013'),
        Produto(nome='Bloco de Notas', descricao='100 folhas', preco=6.90, estoque=80, categoria='Papelaria', sku='BLO014'),
        Produto(nome='Pen Drive 16GB', descricao='USB 3.0', preco=34.90, estoque=15, categoria='Eletrônicos', sku='PEN015'),
        Produto(nome='Mouse Óptico', descricao='USB, alta precisão', preco=39.90, estoque=18, categoria='Eletrônicos', sku='MOU016'),
        Produto(nome='Fichário Escolar', descricao='Com divisórias', preco=49.90, estoque=22, categoria='Acessórios', sku='FIC017'),
        Produto(nome='Livro Didático Matemática', descricao='Ensino Fundamental', preco=79.90, estoque=12, categoria='Livros', sku='LIV018'),
        Produto(nome='Livro Didático Português', descricao='Ensino Fundamental', preco=74.90, estoque=14, categoria='Livros', sku='LIV019'),
        Produto(nome='Garrafa Térmica 500ml', descricao='Mantém temperatura', preco=32.90, estoque=25, categoria='Acessórios', sku='GAR020'),
    ]
    db.session.bulk_save_objects(produtos)
    db.session.commit()

if __name__ == '__main__':
    from app import app
    with app.app_context():
        db.create_all()
        seed()
