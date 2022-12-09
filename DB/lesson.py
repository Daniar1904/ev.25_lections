# PostgresSQL - Система управления базами данных(СУБД, DBMS)
# Это ряд программ и инструментов, позволяющих создавать БД, управлять ею и манипулировать данными внутри БД

# Postgres - сама база данных, она объектно-реалиционная, то есть данные хранятся в виде таблиц и таблицы имеют связи между собой

# SQL (Stuctured Query language) - декоративный язык структурированных запросов, он применяется для создания и получания данных при помощи запросов в БД

# -----------------------------------

# Типы полей в Postgres
# 1. Numeric types:
        # a. smallint(2 bytes) -> -32767 to 32767
        # b. integer(4 bytes) -> -2147000 to 2147000
        # c. bigint(8 bytes) -> ...
        # d. serial(4 bytes) -> auto - increment(integer, 1 - 2147000)
        # e. real(4 bytes) -> число с плавающей точкой, вещественное число
        # f. double precision(8 bytes) -> real но только с двойной точкой

# 2. Character types(строковые типы):
        # a. varchar(кол-во символов 255) - можем указать максимальное кол-во символов вручную, если мы указали максимальное кол-во символов в 50, а заполним всего 10, то остальные 40 сим. останутся пустыми.
        # b. char(255) - если не заполним все символы, то остальные заполнятся пробелами
        # c. text - неограниченное кол-во символов

# 3. Boolean types:
        # boolean(1 bytes) -> True/False

# 4. date - календарная дата(год.месяц.день)
 
# 5. location - координатная точка -> (245, -12) -> (x, y)

# ------------------------------------

# ubuntu: sudo -u postgres psql -> команда для входа в постгрес через корневого пользователя postgres
# psql -> для входа в СУБД через своего юзера

# \q - выход из СУБД

# \du - список всех юзеров

# \l - список всех баз данных

# \c <dbname> -> команда подключения к БД
    # \dt -> список всех таблиц в БД
    # \d <table name> -> подробная информация про таблицу

# ИМПОРТ данных при помощи файла:
# psql -U <ваш юзер нейм> -d <база данных> -f <путь до файла>
# psql -U daniar -d northwind -f /Users/daniar/Desktop/11-fill_in_northwind.sql  !!!EXAMPLE!!!

# CREATE DATABASE <dbname>; -> команда для создания базы данных
# CREATE USER <username> WITH PASSWORD <password>; -> создает юзера

# ALTER USER <username> WITH SUPERUSER; -> команда для изменения статуса юзера на суперюзера

# SELECT <row/colomn> FROM <tablename>;
     # * (ALL)
# -> Команда для получения данных из таблиц


# WHERE: используется для фильтрации по полям будут выводиться только те данные, которые соответствуют условию опера WHERE
# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> = 'чему-либо'

# BETWEEN: Условие 'между'
# SELECT * FROM products WHERE id BETWEEN 3 and 8;

# AND: операор 'и', для множества условий.

# LIKE: Выводит результат который соответствует введеному шаблону для строк. Чувствителен к регистру.
# ILIKE: то же самое только не зависит от регистра.

# ORDER BY: Сортировка по входящим данным по убыванию или возврастанию
        # ASC(по возрастанию) DESC(по убыванию)
# Синтаксис: SELECT <row> FROM <tablename> ORDER BY <row> [ASC/DESC(default)];

# Агрегационные функции - AVG() # среднее, COUNT(), MIN(), MAX(), SUM()

# AS (ALIAS)
# SELECT name, price * quantity AS total FROM produucts;


# GROUP By
# Разделяет данные, которые мы получаем в SELECT'е, при этом группируя их по определенному признаку. И теперь для каждой группы можно использовать функции.
# SELECT city, MAX(temp_high), AVG(prcep), SUM(temp_low) as summa_temp, MIN(date) FROM weather GROUP BY city;

# HAVING: он работает также как и WHERE, только с оператором GROUP BY.


# Команда для создания таблицы 
# CREATE TABLE <tablename> (
#         <name_column> <type>,
#         <name_column> <type>,
#         <name_column> <type>
# );
        # CREATE TABLE weather (city varchar(80),
        #                         date date,
        #                         temp int);

# DROP TABLE <name>; удаление

# Команда для добавления данных в таблицу
# INSERT INTO <tablename> [(columns)] VALUES (data)

# INSERT INTO cities (name, location) 
# VALUES ('Bishkek', '(42, 74)');

# Команда обновления
# UPDATE <tablename> SET <row> = <new_value>
# WHERE <row> = <value>

# Команда для удаления
# DELETE FROM <tablename> WHERE <row> = <value>


 # 5.Location - координатная точка -> (245, -12) -> (x, y)

# ========================================================
# Связи между таблицами(relations):
#     1. Один к одному(One-to-one) - Человек и паспорт
#     2. Один ко многим(One-to-many) - Человек и банковские карты
#     3. Много ко многому(Many to many) - Студенты и преподаватели 

# Ограничения(Constraints):
#     1. NOT NULL
#     2. UNIQUE
#     3. CHECK -> CHECK NUMBER > 5
#     4. PRIMARY KEY(для установки идентификатора данных в таблице)
#     5. FOREIGN KEY(ддля установки связи между таблицами)
#     6. ON DELETE(для установки поведения при удалении данных, которые были связаны)
#     -> SET NULL, CASCADE, RESTRICT, SET DEFAULT(value)

# SELECT p1.title, p1.price, o1.quantity, p1.price * o1.quantity as total_sum FROM products p1, orders o1 WHERE p1.id = 
# o1.product_id; - ЗАпрос сразу в две таблицы


# JOIN - соединение таблиц
# SELECT * FROM products JOIN orders ON products.id = orders.product_id; 

# JOIN: Выборка данных из двух таблиц, соединение таблиц

# LEFT JOIN: Выборка будет содержать все строки из левой таблицы

# RIGHT JOIN: Выборка будет содержать все строки из правой таблицы

# INNER JOIN: выводит все данные согласно условию
