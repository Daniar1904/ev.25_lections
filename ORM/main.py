# ORM (Object_Relational Mapping) - технология программирования, благодаря которой разработчики могут использовать язык программирования для взаимодействия с реляционнной базой данных (PostgreSQL, MySQL и тд), вместо того, чтобы писать операторы SQL, вы будете писать код ООП на языке программирования - это очень сильно ускоряет разработку приложения и бд, особенно на начальных этапах

from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'ormdb',
    user = 'daniar',
    password = '1',
    host = 'localhost',
    port = 5432
)
