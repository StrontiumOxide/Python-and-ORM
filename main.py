from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models as m

def find_book(request) -> None:

    DSN = "postgresql://postgres:qwerty123@localhost:5432/Python and ORM"
    engine = create_engine(url=DSN)
    m.create_tables(engine)

    with sessionmaker(bind=engine)() as session:   
        data = session.query(m.Book.title, m.Shop.name, m.Sale.count, m.Sale.date_sale).\
            select_from(m.Shop).\
            join(m.Stock).\
            join(m.Book).\
            join(m.Publisher).\
            join(m.Sale)

    if request.isdigit():
        data = data.filter(m.Publisher.id == request)

    else:
        data = data.filter(m.Publisher.name == request)

    len_1 = max(map(lambda x: len(str(x[0])), data))
    len_2 = max(map(lambda x: len(str(x[1])), data))
    len_3 = max(map(lambda x: len(str(x[2])), data))

    for title_book, name_shop, price, date in sorted(data):
        print(f'{title_book: <{len_1}} | {name_shop: <{len_2}} | {price: <{len_3}} | {date}')
        
if __name__ == "__main__":
    request = input("Введите имя издателя или его идентификатор: ")
    find_book(request=request)
    