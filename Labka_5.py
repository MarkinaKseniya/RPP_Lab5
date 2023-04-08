# Раздел I. Работа с базой данных Sqlite.
# ------------------------------------------------------
# 1. Функция создания таблицы «users» в базе данных Sqlite для хранения информации о пользователе.
import sqlite3
conn = sqlite3.connect('users')
c = conn.cursor()
c.execute("""create table if not exists users(
id integer primary key,
name text,
email text)""")
conn.commit()

# ------------------------------------------------------
# 2. Функция добавления нового пользователя в таблицу «users»


def insert_value(id, name, email):
    conn = sqlite3.connect('users')
    cursor = conn.cursor()
    cursor.execute("""insert into users  (id, name, email) values (:id,:name,:email) """, {"id":id, "name":name, "email":email} )
    conn.commit()
# ------------------------------------------------------
# 3. Функция для получения всех пользователей из таблицы «users»


def select_func():
    cursor = conn.cursor()
    cursor.execute("""select * from users""")
    print(cursor.fetchall())
# ------------------------------------------------------
# 4. Функция для получения пользователя по id из таблицы «users»


def select_user(id):
    cursor = conn.cursor()
    cursor.execute("""select * from users where id=:id""",{"id":id})
    print(cursor.fetchall())
# ------------------------------------------------------
# 5. Функция для удаления пользователя по id из таблицы «users»


def delete_user(id):
    cursor = conn.cursor()
    cursor.execute("""delete from users where id=:id""",{"id":id})
    print(cursor.fetchall())
    conn.commit()
# ------------------------------------------------------

# Раздел II. Тестирование приложения
# Функция main, которая последовательно выполняет все функции из "Раздела 1"
# Заполнение таблиц данными


def main():
    # insert_value(123,'Ксения','pypka123@mail.ru')
    # insert_value(145, 'Кирилл', 'ezrox@mail.ru')
    # insert_value(158, 'Алексей', 'bombino@mail.ru')
    # insert_value(194, 'Анастасия', 'hannah.montana@mail.ru')
    # insert_value(164, 'Анатолий', 'bebra@mail.ru')
    # insert_value(191, 'Юлия', 'juul@mail.ru')
    # insert_value(208, 'Глеб', 'sad.boy@mail.ru')
    # insert_value(123, 'Юрий', 'loh.pedalniy@mail.ru')
    # insert_value(145, 'Павел', 'pavlyusha@mail.ru')
    # insert_value(158, 'Жанна', 'stuardessa@mail.ru')
    # insert_value(194, 'Джотаро', 'yare.yaredaze@mail.ru')
    # insert_value(164, 'Богдан', 'bogom.dan@mail.ru')
    # insert_value(191, 'Ростислав', 'jaba.zlaya@mail.ru')
    # insert_value(208, 'Маргарита', 'ne.rita@mail.ru')
    select_func() # Вывод всех пользователей
    select_user(194) # Вывод пользователя по id
    delete_user(194) # Удаление пользователя по id
    select_func() # Вывод всех пользователей

main()
conn.close()
