# Встроенные функции

# lambda
# map()
# filter()
# enumerate()
# zip()
# all(), any()

# Анонимные функции - lambda(обычные функции с одной особенностью, у них нет имён)
# lambda функции могут принимать сколько угодно параметров, но всегда возвращают одно выражение.

# def hello(): return 'hello'

# print(hello())

# x = lambda: 'hello'
# print(x())

# x = lambda a, b, c: (a * b) % c
# print(x(5, 5, 2))

# x = lambda num1, num2, degree = None: (num1 * num2) ** degree if degree else num1 * num2
# print(x(2, 2, 3))
# print(x(5, 5))

# def myFunc(n):
#     return lambda num: num * n

# my_doubler = myFunc(2)
# my_tripler = myFunc(3)

# print(my_doubler(50))
# print(my_doubler(150))
# print(my_doubler(500))
# print(my_tripler(1000))
# print(my_tripler(4000))

# dict_ = {
#     'John': 500,
#     'Tirion': 170000,
#     'Tom': 150,
#     'Sanzhar': 20,
#     'Ayana': 100_000
# }

# new_dict = sorted(dict_.items(), key = lambda x: x[1], reverse=True)
# print(dict(new_dict))

# ---------------------

# map(function, iterable) - применяет к каждому элементу внутри iterable функцию, которую мы ей передаем, закидывая в результат те данные, которые возвращает функция, в результате мы получаем mapobject(iterator), в котором хранятся все наши данные.
# Например, с помощью map можно преобразовать все элементы внутри списка. Перевести все строки в верхний регистр.

# ls = ['one', 'two', 'three', 'four', 'five']
# new_ls = list(map(str.capitalize, ls))
# print(new_ls)

# names = ['John', 'Aikol', 'Aizirek', 'Nurayim', 'Sanzhar']

# new_ls = list(map(lambda x: f'Hello mr/mrs {x}', names))
# print(new_ls)

# dict_ = {1: 2, 3: 4, 5: 6}
#         # {1: '2', 3: '4', 5: '6'}

# result = dict(map(lambda x: (x[0], str(x[1])), dict_.items()))
# print(result)

# ---------------------------

# filter(function, iterable) -> применяет ко всем элементам iterable функцию, которую мы передаем и возвращает filterobject(итератор) только с теми элементами для которых функция вернула True.

# ls = ['one', 'two', '3', '', '1', '100', 'John99']

# result = list(filter(str.isdigit, ls))
# print(result)

# ls = ['John', 'one', 'two', 'list', 'makers', 'ev.25', 'fanta']
# res = list(filter(lambda x: len(x) > 4, ls))
# print(res)

# ---------------------------

# enumerate(iterable) - она пронумеровывает каждый элемент внутри iterable её собственным индексом.

# ls = ['str1', 'str2', 'str3']

# # x = list(enumerate(ls))
# # print(x)

# for i, x in enumerate(ls):
#     print(f'Index: {i}, Element: {x}')

