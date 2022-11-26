import sqlite3
from sqlite3 import Error
from parser import array_books

path = './books_app.sqlite'

connection = None

try:
    connection = sqlite3.connect(path)
    print("Подключение к базе данных прошло успешно")
except Error as er:
    print(f"Ошибка подключения - {er}")

cursor = connection.cursor()

create_books_table = """

CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author TEXT NOT NULL,
    name_book TEXT,
    price TEXT,
    genre TEXT,
    publisher TEXT,
    annotation TEXT );
"""

try:
    cursor.execute(create_books_table)
    connection.commit()
    print("Запрос выполнен успешно")
except Error as er:
    print(f"Произошла ошибка - {er}")



def create_sqlite(parameter):
    for data in parameter():
        print(data)
        create_books = """
            INSERT INTO books (author, name_book, price, genre, publisher, annotation)
            VALUES (?, ?, ?, ?, ?, ?);
        """
        cursor.execute(create_books, data)
        connection.commit()

create_sqlite(array_books)

connection.close()