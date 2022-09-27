# Типы данных -> числа int(), float()

# = -> оператор присваивания
# number = 5   
# print(number)
# number = 51
# print(number)

# tomorrow_day -> snake case
# tomorrowDay -> camel case
# abc -> нижний регистр
# ABC -> верхний регистр

# +
# a = 5
# b = 15
# result = a+b 
# print (result)

# print('Результат суммы чисел 5 и 15:', 5 + 15)

# a = 100
# b = 1000
# c = 500
# d = 56.20 
# print(a + b + c + d)

#  -
# num1 = 996
# num2 = 67.55
# print(num2 - num1)

# *
# num1 = int(input('Введите число 1: '))
# num2 = int(input('Введите число 2: '))
# result = num1 * num2
# print('Результат произведения чисел', num1, 'и', num2, 'равно', result)

# num1 = input('Введите число')
# print((num1))
# print(type(num1))

# num = '15'
# num = int(num)
# print(type(num))

# / and // and %
#  / -> обычное деление
#  // -> целочисленное деление(деление без остатка)
#  % -> остаток без деления(остаток от деления

# num1 = 5
# num2 = 2
# print(num1 / num2)
# print(num1 // num2)
# print(num1 % num2)

# ** - возведение в степень

# num1 = 5
# print(num1 ** 10000)


# pow(a, b) -> функция возведения числа а в степень b
# print(pow(2, 5, 5))
#  2 ** 5 % 5 -> 2

# divmod(a, b) -> она вводит два числа, первое число - это результат целочисленного деления(//), 
# а второе число это модульное деление(%) двух чисел

# res = divmod(4, 5)
# print(res)

# round() -> функиця округления числа
# res = (24 / 13)
# print(round(res, 1))

# abs() - абсолютное значение -> abs(-5) 
# = 5 -> |5| = 5
# print(abs(-101))
# print(abs(50))

# -----------------------

# import math
# from math import pi, sqrt 
# print(pi)
# print(sqrt(25))
# print(math.pi)
# print(math.sqrt) -> корень числа 
# print(math.sqrt(25))
# print(math.sqrt(101))
# print(math.sqrt(6))

# dir() - возвращает методы объекта или функции модуля
# import math
# print(dir(math))

# Множественное присваивание
# a = 5
# a, b, c = 1, 2, 3
# v = 5
# n = 7
# d = 3

# v, n, d = d, v, n 
# print(v, n, d)

# num1 = 10
# num2 = 3
# num3 = num1
# num1 = num2
# num2 = num3
# print(num1, num2)

# print('hello' * 3) дублирование строк 

# str1 = '12'
# num1 = 2
# print(str1 + str(num1))

# Инкремент и дикремент

# Инкремент - увеличение значения какой-либо переменной a = 1 (a += 1 -> a = a + 1)

# a = 0
# # a +=1 
# a = a + 1
# print(a)

# Дикремент - уменьшение значения какой-либо переменной (a -= 1 -> a - 1)
# a = 0
# a -= 1
# print(a)

# * 
# a = 5
# a *= a
# print(a)

#  /
# a = 10
# a /= 2
# print(a)

# a = 7
# a %= 2
# print(a)

# id() - возвращает номер ячейки памяти
# a = 2
# b = 1
# print(id(a))
# print(id(b))

# type() -> выводит тип заданной переменной
# a = 9
# b = 'hello'
# print(type(a))
# print(type(b))

# var = int(input('Введите число'))

# num1 = int(input('Введите число:'))
# num2 = int(input('Введите степень:'))
# print(num1 ** num2)

# Модуль random - предоставляет функции для генерации случайных чисел, букв, символов
# import random

# print(dir(random))

# num = random.randint(111111, 999999)
# print(num)

# from random import choice

# import string
# # print(string.ascii_letters)
# a = choice(string.ascii_letters)
# print(a)


# import math

# from math import pi

# r = int(input('Введите радиус:'))
# s = (math.pi * (r ** 2))
# p = ((2 * r) * math.pi)
# print(round(s))
# print(round(p))




