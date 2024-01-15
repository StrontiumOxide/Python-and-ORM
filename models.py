import sqlalchemy as sql
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.Text, nullable=False)

    def __str__(self) -> str:
        return f'Издатель: "{self.name}" №{self.id}'
    
class Book(Base):
    __tablename__ = "book"

    id = sql.Column(sql.Integer, primary_key=True)
    title = sql.Column(sql.Text, nullable=False)
    id_publisher = sql.Column(sql.Integer, sql.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref="publisher")

    def __str__(self) -> str:
        return f'Книга: "{self.title}" №{self.id}, id издательства: {self.id_publisher}' 

class Shop(Base):
    __tablename__ = "shop"

    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.Text, nullable=False)

    def __str__(self) -> str:
        return f'Книга: "{self.name}" №{self.id}'

class Stock(Base):
    __tablename__ = "stock"

    id = sql.Column(sql.Integer, primary_key=True)
    id_book = sql.Column(sql.Integer, sql.ForeignKey("book.id"), nullable=False)
    id_shop = sql.Column(sql.Integer, sql.ForeignKey("shop.id"), nullable=False)
    count = sql.Column(sql.Integer, nullable=False)

    book = relationship(Book, backref="book")
    shop = relationship(Shop, backref="shop")

    def __str__(self) -> str:
        return f'id: "{self.id}", id-книги: {self.id_book}, id-магазина: {self.id_shop}, Количество книг: {self.count}'

class Sale(Base):
    __tablename__ = "sale"

    id = sql.Column(sql.Integer, primary_key=True)
    price = sql.Column(sql.Integer, nullable=False)
    date_sale = sql.Column(sql.DATE, nullable=False)
    id_stock = sql.Column(sql.Integer, sql.ForeignKey("stock.id"), nullable=False)
    count = sql.Column(sql.Integer, nullable=False)

    stock = relationship(Stock, backref="stock")

    def __str__(self) -> str:
        return f'id: "{self.id}", Цена книги: {self.price}, Дата покупки: {self.date_sale}, id-запаса: {self.id_stock}, Количество проданного: {self.count} '

def create_tables(engine):
    Base.metadata.create_all(engine)

