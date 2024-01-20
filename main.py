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

















#Здесь может быть какой-то код


# def get_shops(...): #Функция принимает обязательный параметр
#     ... = db_session.query( #Создаем общее тело запроса на выборку данных и сохраняем в переменную
#         ..., ..., ..., ..., #Название книги, имя магазина, стоимость продажи и дату продажи
#     ).select_from(...).\ #Из таблицы магазинов
#         join(...).\ #Объединяем с таблицей стоков
#         join(...).\ #Объединяем с таблицей книг
#         join(...).\ #Объединяем с таблицей публицистов
#         join(...).\ #Объединяем с таблицей продаж
    
#     if ....isdigit(): #Проверяем переданные данные в функцию на то, что строка состоит только из чисел
#         ... = ....filter(... == ...).all() #Обращаемся к запросу, который составили ранее, и применяем фильтрацию, где айди публициста равно переданным данным в функцию, и сохраняем в переменную
#     else:
#         ... = ....filter(... == ...).all() #Обращаемся к запросу, который составили ранее, и применяем фильтрацию, где имя публициста равно переданным данным в функцию, и сохраняем в переменную
#     for ..., ..., ..., ... in ...: #Проходим в цикле по переменой, в которой сохранянен результат фильтрации, и при каждой итерации получаем кортеж и распаковываем значения в 4 переменные
#         print(f"{...: <40} | {...: <10} | {...: <8} | {....strftime('%d-%m-%Y')}") #Передаем в форматированную строку переменные, которые содержат имя книги, название магазина, стоимость продажи и дату продажи


# if __name__ == '__main__':
#     ... = input("...: ") #Просим клиента ввести имя или айди публициста и данные сохраняем в переменную
#     get_shops(...) #Вызываем функцию получения данных из базы, передавая в функцию данные, которые ввел пользователь строкой выше    


