from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    descricao = db.Column(db.Text)
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
    categoria = db.Column(db.String(30), nullable=False)
    sku = db.Column(db.String(30))

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': self.preco,
            'estoque': self.estoque,
            'categoria': self.categoria,
            'sku': self.sku
        }

@app.route('/produtos')
def get_produtos():
    produtos = Produto.query.all()
    return jsonify([p.to_dict() for p in produtos])

def criar_produtos():
    with app.app_context():
        db.create_all()
        produtos = [
            Produto(nome='Caderno Universitário', descricao='Capa dura, 200 folhas', preco=24.90, estoque=50, categoria='Papelaria', sku='CAD001'),
            Produto(nome='Caneta Esferográfica Azul', descricao='Ponta fina, tinta azul', preco=2.50, estoque=200, categoria='Papelaria', sku='CAN002'),
            Produto(nome='Lápis de Cor 12 cores', descricao='Estojo com 12 cores', preco=15.90, estoque=80, categoria='Papelaria', sku='LAP003'),
            Produto(nome='Mochila Escolar', descricao='Mochila resistente, vários bolsos', preco=89.90, estoque=30, categoria='Acessórios', sku='MOC004'),
            Produto(nome='Borracha Branca', descricao='Borracha macia', preco=1.80, estoque=150, categoria='Papelaria', sku='BOR005')
        ]
        db.session.bulk_save_objects(produtos)
        db.session.commit()
        print("Banco de dados criado e produtos inseridos com sucesso!")

if __name__ == '__main__':
    criar_produtos()  # Cria o banco e insere os produtos
    app.run(debug=True)  # Inicia o servidor

@app.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = Produto.query.all()
    return jsonify([p.to_dict() for p in produtos]), 200

@app.route('/produtos', methods=['POST'])
def add_produto():
    data = request.json
    if not data.get('nome') or len(data['nome']) < 3:
        return jsonify({'error': 'Nome inválido'}), 400
    produto = Produto(
        nome=data['nome'],
        descricao=data.get('descricao', ''),
        preco=data['preco'],
        estoque=data['estoque'],
        categoria=data['categoria'],
        sku=data.get('sku', None)
    )
    db.session.add(produto)
    db.session.commit()
    return jsonify(produto.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
