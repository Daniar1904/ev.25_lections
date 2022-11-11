# def time(**kwargs):
#     employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]
#     while 'overTime' > 0:

# list_ = [False, True, False, True, False, True, False, True, False, True]
# list2 = [1 for x in list_ if x == True]
# print(list2)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# list_name = [len(x) for x in list_name]
# print(list_name)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# dict_ = {x: len(x) ** 2 for x in list_name if len(x) > 4}
# print(dict_)

# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# dict2 = [key.upper() for key, value in dict_.items() if value in range(200, 5000)]
# print(dict2)

# list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
# list2 = []
# print(list2)

# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# b = {k: range(v) for k, v in a.items()}
# print(b)

# dict_ = {'first': 1, 'second': 2, 'third': 3}
# a = {k: 'odd' if v % 2 != 0 else 'even' for k, v in dict_.items()}
# print(a)

# lang = 'en'
# for x in lang:
#   if x == 'en':
#     print('This is english')

# string = '123456'
# for x in string.split():
#   if x[0] + x[1] + x[2] == x[3] + x[4] + x[5]: !!!
#     print('Да')
#   else:
#     print('Нет')

# age = int(input('Введите возраст'))
# if age < 18:
#   print('Доступ запрещен')
# else:
#   print('Добро пожаловать')

# number = int(input())
# if number == range(3, 6):
#   print('весна')
# elif number == range(6, 9):
#   print('лето')
# elif number == range(9, 12):
#   print('осень')
# elif number == '12' or '1' or '2':
#   print('зима')

# string = input()
# if string.isdigit():
#   print('is digit')
# elif string.isalpha():
#   print('is alpha')
# else:
#   print('is ASCII')

# a = int(input())
# b = int(input())
# c = int(input())
# if a + b > c:
#   print('yes')
# elif b + c > a:
#   print('yes')
# elif a + c > b:
#   print('yes')
# else:
#   print('no')

# n = int(input())
# if n == 1 or n % 11 == 0:
#   print(f'На лугу пасется {n} корова')
# elif n == 2 or n == 3 or n == 4 or n[1] == 2 or n[1] == 2 or n[1] == 3 or n[1] == 4:
#   print(f'На лугу пасется {n} коровы')
# else:
#   print(f'На лугу пасется {n} коров')

# a = int(input())
# if a % 2 != 0:
#   print('первый')
# else:
#   print('второй')

# import functools
# def multiply_list(*args):
#   res = functools.reduce(lambda x, y: x * y, args)
#   return res
# print(multiply_list(1, 2, 3, 4, 5, 6))

# def func11(a, b, c):
#   try:
#     res = a + b // c
#     return res
#   except ZeroDivisionError:
#     return a + b
# print(func11(1, 2, 0))

