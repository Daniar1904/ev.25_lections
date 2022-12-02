# class Circle:
#     def __init__(self, color='blue', pi=3.14, radius=5) -> None:
#         self.color = color
#         self.pi = pi
#         self.radius = radius
    
#     def info(self):
#         self.ploshad = self.pi * self.radius ** 2
#         return self.ploshad

# obj1 = Circle()
# print(obj1.info())

# class PhoneBook:
#     def __init__(self, name, last_name, number) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.number = number
    
#     def get_info(self):
#         return f'Контакт: {self.name} {self.last_name}, телефон: {self.number}'

# obj = PhoneBook('Bob', 'Bobbie', '0555567567')
# print(obj.get_info())

# class Taxi:
#     def __init__(self, name, price=int, km=int) -> None:
#         self.name = name
#         self.price = price
#         self.km = km
    
#     def Namba(self):
#         price = self.price * self.km
#         return f'{self.name}: {price}'
#     def Yandex(self):
#         price = self.price * self.km
#         return f'{self.name}: {price}'
    

# obj = Taxi('Jorgo', 500, 2)
# print(obj.Namba())
# obj1 = Taxi('Yandex', 600, 4)
# print(obj.Yandex())

# class Class1:
#     def first(self):
#         pass
#     def second(self):
#         pass

# class Class2(Class1):
#     def third(self):
#         pass
#     def fourth(self):
#         pass

# obj = Class2()
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()

# class A:
#     def method1(self):
#         print('Основной функционал')

# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')
        
# obj = B()
# obj.method1()

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
    
#     def display(self):
#         return f'name:{self.name}, age:{self.age}'

# class Student(Person):
#     def __init__(self, name, age, faculty) -> None:
#         super().__init__(name, age)
#         self.faculty = faculty

#     def display_student(self):
#         return f'name:{self.name}, age:{self.age}, faculty:{self.faculty}'

# obj_student = Student('Rick', 21, 'science')
# print(obj_student.display())
# print(obj_student.display_student())

# class ContactList(list):
#     def search_by_name(self, names):
#         self.name = names
#         for name in names:

# class SmartPhones:
#     def __init__(self, name, color, memory) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = 0

#     def __str__(self) -> str:
#         return f'{self.name} {self.memory}'

#     def charge(self, p):
#         self.battery += p

# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, ios) -> None:
#         super().__init__(name, color, memory)
#         self.ios = ios
    
#     def send_imessage(self, stroka):
#         self.stroka = stroka
#         return f'sending {self.stroka} from {self.name} {self.memory}'

# class Samsung(SmartPhones):
    
#     def __init__(self, name, color, memory, android) -> None:
#         super().__init__(name, color, memory)
#         self.android = android

#     def show_time(self):
#         from datetime import datetime
#         return datetime.now().time()

# phone = SmartPhones('generic', 'blue', '128GB')
# print(phone)
# print(phone.battery)
# phone.charge(20)
# print(phone.battery)
# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3')
# print(iphone7)
# print(iphone7.send_imessage('hello'))
# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo')
# print(samsung21.show_time())

# class Taxi:
#     def __init__(self, name, cost, cost_km) -> None:
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km
    
#     def get_total_cost(self, km):
#         self.km = km
#         return f'Такси {self.name}, стоимость поездки: {self.cost + self.cost_km * self.km} сом'

# taxi1 = Taxi('Namba', 40, 15)
# print(taxi1.get_total_cost(4))
# taxi2 = Taxi('Yandex', 50, 2)
# print(taxi2.get_total_cost(7))
# taxi3 = Taxi('Jorgo', 80, 6)
# print(taxi3.get_total_cost(9))

# class Phone:
#     def __init__(self, name, last_name, phone) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
    
#     def get_info(self):
#         return f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}'

# contact = Phone('John', 'Snow', '0707707707')
# print(contact.get_info())

# class Salary:
#     percent = 8
#     def __init__(self, salary, experience) -> None:
#         self.salary = salary
#         self.experience = experience


#     def count_percent(self):
#         return self.salary * self.percent / 100 * self.experience

# obj = Salary(10000, 10)
# print(obj.count_percent())

# class Nobel:
#     def __init__(self, category, year, winner) -> None:
#         self.category = category
#         self.year = year
#         self.winner = winner

#     def get_year(self):


# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [x for x in list_ if x < 0]
# print(int_list)
# int_list = []
# for x in list_:
#     if x < 0:
#         x = 1
#         int_list.append(x)
#     else:
#         int_list.append(x)

# print(int_list)


# class MyDict(dict):
#     def get(self, object):
#         if not object:
#             return 'Are you kidding?'
#         return dict.get(object)

# obj_dict = MyDict({'some_title:': 2})
# print(obj_dict.get('some'))

# class Circle:
#     color = 'синий'
#     pi = 3.14
#     def __init__(self, radius, color = 'синий') -> None:
#         self.radius = radius

#     def get_area(self):
#         return Circle.pi * self.radius ** 2

# circle = Circle(2)
# circle.color = 'Red'
# print(circle.color)
# print(circle.get_area())

# class Password:
#     password = ['12345678', 'rdyctfvgyhbkjnk', 'ftuy']
#     def validate(self):
#         for passw in Password.password:
#             if not len(passw) >= 8 and len(passw) < 15:
#                 print('Password should be longer than 8, and less than 15')
#             elif not isinstance(passw, int):
#                 print('Password should contain numbers too')
#             elif not isinstance(passw, str):
#                 print('Password should contain letters as well')
#             for x in passw:
#                 if x != '@' or x != '#' or x != '&' or x != '%' or x != '~' or x != '*':
#                     print('Your password should have some symbols')
#         return 'Ваш пароль сохранен.'

#     def __str__(self) -> str:
#         Password.password = '*'

# obj = Password()
# print(obj.validate())

# class Song:
#     def __init__(self, title, name, year) -> None:
#         self.name = name
#         self.title = title
#         self.year = year

#     def show_author(self):
#         return f'Автор этой песни {self.name}'
        
#     def show_title(self):
#         return f'Название этой песни {self.title}'
    
#     def show_year(self):
#         return f'Эта песня вышла в {self.year} году'

# song = Song('Happy', 'Pharrell Williams', 2013)
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())

# a = input()
# list_ = []
# for x in a.split(','):
#     list_.append(x)
# tuple_ = a
# tuple_.split(',')
# print(list_)
# print(tuple_)

# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# new_list = []
# a = input()
# for word in list_:
#     if word[0] == a:
#         new_list.append(word)

# print(new_list)

# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
# repeats = 4
# res = []
# for x in list_:
#     if list_.count(repeats) == x:
#         res.append(x)

# print(res)







