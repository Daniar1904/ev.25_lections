# Принципы ООП:
# 1. Наследовалние
# 2. Инкапсуляция
# 3. Полиморфизм

# 4. Абстракция
# 5. Композиция
# 6. Агрегация
# 7. Ассоциация

# -------------------

# Наследование
# Позволяет принимать родительские методы и атрибуты для дочернего класса

# Родительский класс
# Дочерний класс

# -------------------------------------------------------------------------

# class Animal:
#     def print_info(self):
#         print('I\'m an animal!')

# class Croco(Animal):
#     pass

# croco = Croco()
# croco.print_info()

# --------------------------------=

# class Animal:
#     name = None
#     golos = None
#     meal = None

#     def say(self):
#         print(f'This animal is {self.name}: {self.golos}')
    
#     def eat(self):
#         print(f'This animal {self.name} eats {self.meal}!')

# class Lion(Animal):
#     name = 'lion'
#     meal = 'meat'
#     golos = 'aarrrr!'
#     griva = True

#     def print_info(self):
#         print(f'Griva: {self.griva}')

# class Dog(Animal):
#     name = 'dog'
#     meal = 'meat'
#     golos = 'bark!'

# class Koala(Animal):
#     name = 'koala'
#     meal = 'efkalipt'
#     golos = 'roooaar!'

# rex = Dog()
# simba = Lion()
# julian = Koala()

# rex.say()
# rex.eat()

# simba.say()
# simba.eat()
# simba.print_info()

# julian.say()
# julian.eat()

# ----------------------------

# class Employee:
#     bonus = 1.5
#     def __init__(self, name, last_name, salary) -> None:
#         self.name = name + ' ' + last_name
#         self.salary = salary

#     def get_info(self):
#         return f'FIO: {self.name}, Salary: {self.salary}'

#     def give_increase(self):
#         self.salary = self.salary * self.bonus

# class Developer(Employee):
#     def __init__(self, name, last_name, salary, language) -> None:
#         super().__init__(name, last_name, salary)
#         self.prog_lang = language

# class Manager(Employee):
#     def __init__(self, name, last_name, salary, emps = None) -> None:
#         super().__init__(name, last_name, salary)
#         if not emps:
#             self.emps = []
#         else:
#             self.emps = emps

#     def add_emp(self, employee):
#         self.emps.append(employee)

#     def show_emps(self):
#         return [x.get_info() for x in self.emps]


# dev1 = Developer('John', 'Snow', 1000, 'Python')
# dev2 = Developer('Steve', 'Jobs', 3000, 'C++')
# dev3 = Developer('Lary', 'Page', 1500, 'JS')
# dev4 = Developer('Raychel', 'Cruse', 1000, 'Python')
# man1 = Manager('Ivan', 'Ivanov', 2000)
# man2 = Manager('Dastan', 'Velikiy', 4000, [dev1, dev4])

# man1.add_emp(dev2)
# man1.add_emp(dev3)
# man2.add_emp(dev2)

# print(f'Manager: {man1.get_info()}, has {man1.show_emps()} developers.')
# print(f'Manager: {man2.get_info()}, has {man2.show_emps()} developers.')

# man2.give_increase()
# dev2.give_increase()
# print(man2.get_info())
# print(dev2.get_info())

# --------------------------------------------------------------------------

# class Person:
#     def __init__(self, name, last_name, age) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.age = age
    
#     def info(self):
#         print(f'My name is {self.name} {self.last_name}, and I\'m {self.age} years old!')

# class Student(Person):
#     def __init__(self, name, last_name, age, univer) -> None:
#         super().__init__(name, last_name, age)
#         self.univer = univer

#     def info(self):
#         super().info()
#         print(super(), '------------')
#         print(f'I\'m study in {self.univer}!')

# obj = Student('Kyle', 'Walker', 23, 'KGTU')
# obj.info()

# ------------------------------------------------

# class Laptop:
#     def __init__(self, brand, model, description, price, ) -> None:
#         self.brand = brand
#         self.model = model
#         self.desc = description
#         self.price = price

#     def get_info(self):
#         return {'brand': self.brand, 'model': self.model, 'description': self.desc, 'price': self.price}

# class Macbook(Laptop):
#     def __init__(self, brand, model, description, price, year, provider) -> None:
#         super().__init__(brand, model, description, price)
#         self.year = year
#         self.provider = provider
    
#     def get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['provider'] = self.provider
#         return repr

# class Acer(Laptop):
#     def __init__(self, brand, model, description, price, videocard, display) -> None:
#         super().__init__(brand, model, description, price)
#         self.videocard = videocard
#         self.display = display
    
#     def get_info(self):
#         repr = super().get_info()
#         repr['videocard'] = self.videocard
#         repr['display'] = self.display
#         return repr

# obj1 = Laptop('Acer', 'M330', '8gb, 512 SSD', 800)
# obj2 = Macbook('Apple', 'Air', '13, 8bg, 256 SSD', 1000, 2020, 'China')
# obj3 = Acer('Acer', 'Inspire', '16gb, 1TB SSD', 1000, 'GTX Geforce Nvidia', '15.6 FULL RGB')

# print(obj1.get_info())
# print(obj2.get_info())
# print(obj3.get_info())

# ---------------------------------------------------------------------

# class Post:
#     def __init__(self, user) -> None:
#         self.user = user
#         self.posts = []
#         self.id = 0
    
#     #CRUD
#     def create_post(self, title, body, image):
#         self.id += 1
#         post = dict(id = self.id, title = title, body = body, image = image)
#         self.posts.append(post)
#         return {'status': 201, 'msg': 'Successfully created!'}

#     def lists_posts(self):
#         repr = []
#         for post in self.posts:
#             repr.append({'id': post['id'], 'title': post['title'], 'image': post['image']})
#         return {'status': 200, 'msg': repr}

#     def detail_post(self, id):
#         for post in self.posts:
#             if post.get('id') == id:
#                 return {'status': 200, 'msg': post}
#         return {'status': 404, 'msg': 'Not found!'}

#     def update_post(self, id, **kwargs):
#         for post in self.posts:
#             if post['id'] == id:
#                 post.update(kwargs)
#                 return {'status': 206, 'msg': 'Successfully updated!'}
#         return {'status': 404, 'msg': 'Not found!'}

#     def delete_post(self, id):
#         for post in self.posts:
#             if post['id'] == id:
#                 try:
#                     self.posts.remove(post)
#                     return {'status': 204, 'msg': 'Successfully deleted!'}
#                 except:
#                     return {'status': 500, 'msg': 'Пни своего бэка'}
#         return {'status': 404, 'msg': 'Not found!'}
        
# acc1 = Post('JamesKirk')
# print(acc1.create_post('Good news', 'Я скоро буду отцом!', 'https://foto.jpg'))
# print(acc1.create_post('На чиле', 'На расслабоне', 'https://foto123.jpg'))
# print(acc1.create_post('Я гулял', 'На улице было прекрасно', 'https://image.jpg'))

# print(acc1.lists_posts())
# print(acc1.detail_post(2))
# print()
# print(acc1.detail_post(3))
# print(acc1.update_post(3, title = 'Мы гуляли'))
# print(acc1.detail_post(3))

# print(acc1.delete_post(2))
# print()
# print(acc1.lists_posts())

# TASKS
# class BankAccount:
#     def __init__(self):
#         self.balance = 0

#     def withdraw(self, amount):
#         # if amount > self.balance:
#         #     print('Недопустимая сумма!')
#         #     return
#         self.balance -= amount
#         print(f'Ваш баланс: {self.balance} сом')

#     def deposit(self, amount):
#         # if amount < 0:
#         #     print('Недопустимая сумма!')
#         #     return
#         self.balance += amount
#         print(f'Ваш баланс: {self.balance} сом')

# account = BankAccount()
# account.deposit(1000) 
# account.withdraw(500)

# --------------------------------------------------

# class MyString(str):
#     def __init__(self, value) -> None:
#         self.string = value
#     def append(self, value: str):
#         self.string = self.string + value
#     def pop(self):
#         # StringHello
#         #StringHell
#         removed = self.string[-1]
#         self.string = self.string[:-1]
#         return removed
#     def __str__(self) -> str:
#         return self.string


# example = MyString("String")
# example.append('hello')
# print(example)

# print(example.pop())
# print(example)

# -----------------------------------------

# class CustomError(Exception):
#     def __init__(self, error_name) -> None:
#         self.error = error_name
    
#     def __str__(self) -> str:
#         return f'{self.error}'

# def check_letters(str1):
#     if str1.isupper():
#         return f'ВСЕ ОТЛИЧНО! {str1}'
#     else:
#         raise capitals_error

# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# print(check_letters("HELLO"))


# class Song:
#     def __init__(self, title, name, year) -> None:
#         self.title = title
#         self.name = name
#         self.year = year
#     def show_title(self):
#         return f'Название этой песни {self.title}'

#     def show_author(self):
#         return f'Автор этой песни {self.name}'
    
#     def show_year(self):
#         return f'Эта песня вышла в {self.year} году'

# song = Song('Happy', 'Pharrell Williams', 2013)
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())


class Circle:
    def __init__(self, color='blue', pi=3.14, radius=2) -> None:
        self.color = color
        self.pi = pi
        self.radius = radius
    
    def info(self):
        self.ploshad = self.pi * self.radius ** 2
        return self.ploshad

obj1 = Circle()
print(obj1.info())
