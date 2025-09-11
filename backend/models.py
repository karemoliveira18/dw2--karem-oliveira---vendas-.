from sqlalchemy import Column, Integer, String, Float, Text, DateTime, func
from .database import Base


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False, index=True)
    descricao = Column(Text, nullable=True)
    image_url = Column(String(300), nullable=True)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False, default=0)
    categoria = Column(String(50), nullable=True)
    sku = Column(String(50), nullable=True)

    def __repr__(self):
        return f"<Produto id={self.id} nome={self.nome} preco={self.preco} estoque={self.estoque}>"


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    total_final = Column(Float, nullable=False)
    data = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Pedido id={self.id} total={self.total_final}>"

from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)
    categoria = Column(String, nullable=False)
    sku = Column(String)
