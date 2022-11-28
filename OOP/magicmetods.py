# Magic Methods (магические методы)
# dunder methods (double undescore) -> __init__
# Служебные методы


# res = 5 + 5 # __add__
# print(res)

# class A(int):
#     pass

# obj = A()
# print(dir(obj))

# Магические методы сравнения:
# __eq__(self, other) -> 5 == 8

# __ne__(self, other) -> !=

# __lt__(self, other) -> <

# __gt__(self, other) -> >

# __le__(self, other) -> <=

# __ge__(self, other) -> >=

# print('15' > 'Abc')

# class Word(str):
#     # def __init__(self, word) -> None:
#     #     super().__init__()
#     #     self.word = word
#     def __new__(cls, obj):
#         # print(cls, '!!!!!!!!!')
#         # print(object, '--------')
#         obj = obj.replace(' ', '')
#         return super().__new__(cls, obj)

#     def __gt__(self, __x: str) -> bool:
#         print('gt сработал')
#         print(self, '!!!')
#         print(__x, 'X')
#         return len(self) > len(__x)

#     def _eq__(self, __x: str) -> bool:
#         return len(self) == len(__x)

# obj = Word('     He l l o    ')
# obj1 = Word('    Salam!    ')
# print(obj > obj1)
# print(obj <= obj1)
# print(obj == obj1)
# print(obj, len(obj))
# print(obj1, len(obj1))

# ------------------------

# Конструктор -> __new__
# Инициализатор -> __init__

# class Conventer(float):
#     def __new__(cls, x):
#         print('New сработал!')
#         print(cls)
#         if x < 50:
#             raise ValueError('X меньше 50!')
#         return super().__new__(cls, x)
    
#     def __init__(self, x) -> None:
#         print('init сработал!')
#         print(self)
#         self.number = x

# obj = Conventer(49)
# print(obj)

# ------------------------------------

# Дандер методы для строкового отображения объекта
# __str__
# __repr__

# class Base:
#     def __init__(self, stroka) -> None:
#         self.string = stroka
    
#     def __str__(self) -> str:
#         return f'Объект: {self.string}'

#     def __repr__(self) -> str:
#         return f'Base("{self.string}")'
        
# obj = Base('Jasy')
# print(obj)
# print(repr(obj))
# obj2 = eval(repr(obj))
# print(obj2, '!!!')

# -----------------------------------------

# + - / * // % **

# + -> __add__
# - -> __sub__
# * -> __mul__
# // - > __floordiv__
# / - > __div__
# % -> __mod__
# ** -> __pow__

# class Cifra(int):
#     def __new__(cls, number):
#         if not 0 < number < 100:
#             raise ValueError('Enter the numbers in range 0-100!')
#         instance = super().__new__(cls, number)
#         return instance

#     def __init__(self, number) -> None:
#         self.number = number
    
#     def __add__(self, __x: int) -> int:
#         print('Add вызван')
#         print(f'Result:{self} + {__x} = {self.number + __x.number} :)')
    
# value1 = Cifra(17)
# value2 = Cifra(56)
# value1 + value2


# class User:
#     def __init__(self, name) -> None:
#         self.name = name

#     def __call__(self):
#         print(f'User object: {self.name}')

# user1 = User('Jasy Lili')
# user2 = User('Sherman Mclaren')
# print(callable(user1))
# user1()
# user2()


# class LogSetFile:
#     def __init__(self, file) -> None:
#         self.file = file
#         self.number = 0

#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             from datetime import datetime
#             self.number += 1
#             with open(self.file, 'a') as file:
#                 file.write(f'{self.number}. Func name: {func.__name__}, Called time: {datetime.now().time()}\n')
#             return func(*args, **kwargs)
#         return wrapper

# test = LogSetFile('log.txt')

# @test
# def start_test():
#     pass

# @test
# def hello():
#     pass

# @test
# def world():
#     pass

# start_test()
# hello()
# world()
# start_test()

# ------------------------------------------------------------------

# class MyList(list):
#     def __init__(self, ls):
#         self.ls = ls

#     def __getitem__(self, index):
#         if index == 0:
#             print('Invalid index!')
#         elif index < 0:
#             print(self.ls[index])
#         else:
#             print(self.ls[index - 1])

# x = MyList([1, 2, 3, 4, 5])
# x[-1]
# x[4]
# x[2]
# x[0]