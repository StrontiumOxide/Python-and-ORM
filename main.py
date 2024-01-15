from sqlalchemy import create_engine
import models as m
import psycopg2

DSN = "postgresql://postgres:qwerty123@localhost:5432/Python and ORM"
engine = create_engine(url=DSN)
m.create_tables(engine)

# ---------------------------------------------------------------------------------

def find_book(name: str) -> list:

    with psycopg2.connect(database="Python and ORM", user="postgres", password="qwerty123") as connect:
        with connect.cursor() as cursor:
            cursor.execute(
                query="""
                    SELECT b.title AS "Название книги", 
                            p.name AS "Название издательства", 
                            sl.price AS "Цена книги",
                            sl.date_sale AS "Дата покупки"
                            FROM sale sl
                    JOIN stock st ON st.id = sl.id_stock 
                    JOIN book b ON b.id = st.id_book 
                    JOIN publisher p ON p.id = b.id_publisher 
                    JOIN shop s ON s.id = st.id_shop
                    WHERE p.name = '%s';
    """ % (name,)
            )

            return list(cursor.fetchall())
        
name = input("Введите издательство: ")

for element in sorted(find_book(name)):
    print(" | ".join(list(map(str, element))))



