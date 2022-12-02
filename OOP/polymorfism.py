# Функция полиморфизм -> len() : len 

# print(len('makers'))
# print(len([1,2, 'str', 4,5]))
# print(len({1: '1', 2: '2'}))

# # + (add) - метод полиморфизм
# print(5+5)
# print('hello'+'hello')
# print([1,2,3]+[4,5,6])

# Полиморфизм - способность функции(метода) использоваться для разных типов(классов).
# Широко распростарненное определение: "Один интерфейс - много реализаций".
# list.pop
# set.pop
# dict.pop

# class Cat: 
#     def init(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'it is a cat. Cat\'s name is {self.name}, age {self.age}')

#     def make_sound(self):
#         print(('meow, meow!'))

# class Dog:
#     def init(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'it is a dog. Dog\'s name is {self.name}, age {self.age}')

#     def make_sound(self):
#         print(('bark, bark!'))


# cat = Cat('Garfield', 7)
# dog = Dog('Pluto', 9)

# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()


# from math import pi

# class Shape:
#     def init(self, name) -> None:
#         self.name = name

#     def area(self):
#         pass

#     def fact(self):
#         return f'Я фигура в двумерной плоскости {self.name}'

# class Square(Shape):
#     def init(self, length) -> None:
#         super().init('Квадрат')
#         self.length = length

#     def area(self):
#         return self.length ** 2

#     def fact(self):
#         return 'Все стороны равны и все углы 90 градусов'

# class Circle(Shape):
#     def init(self, radius) -> None:
#         super().init(' Круг')
#         self.radius = radius

#     def area(self):
#         return pi*(self.radius**2)

    
# a = Square(6)
# b = Circle(4)

# print(a.fact())
# print(b.fact())

# print(a.area())
# print(b.area())

# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.

# class Phone:
#     def init(self, imei, os) -> None:
#         self.__imei = imei
#         self.__os = os
#         self.__battery_level = 100

#     @property
#     def battery_level(self):
#         if self.__battery_level < 0.5:
#             raise Exception('Телефон разряжен!')
#         print(f'Уровень заряда = {self.__battery_level}')
#         self.__battery_level -= 0.5

#     @property  
#     def get_info(self):
#         if self.__battery_level < 0.5:
#             raise Exception('Телефон разряжен!')
#         print(f'OS: {self.__os}, IMEI: {self.__imei}')
#         self.__battery_level -= 0.5

#     def play_music(self):
#         if self.__battery_level < 5:
#             raise Exception('Телефон разряжен!')
#         print('Слушаем Мирбу!!!')
#         self.__battery_level -= 5

#     def play_video(self):
#         if self.__battery_level <= 10:
#             raise Exception('Недопустимый уровень заряда!!!')
#         print('Смотрим Историю на ночь:)')
#         self.__battery_level -= 7

#     def charge_battery(self, sec):
#         from datetime import datetime, timedelta
#         from time import sleep

#         now = datetime.now
#         end_time = (now() + timedelta(seconds=sec)).strftime('%M:%S')
#         while now().strftime('%M:%S') != end_time:
#             sleep(1)
#             # print(now().strftime('%M:%S'), end_time)
#             if self.__battery_level < 100:
#                 self.__battery_level += 1
#             print(f'Зарядка. Ваш уровень заряда {self.__battery_level}')


# phone = Phone('123 12313 234', 'IOS 16.2')

# phone.battery_level
# phone.battery_level
# phone.get_info
# phone.battery_level
# phone.play_music()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.battery_level
# phone.charge_battery(30)
# phone.battery_level