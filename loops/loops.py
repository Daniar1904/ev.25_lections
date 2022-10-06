# Циклы - это конструкция, при помощи которых можно организовать многократное исполнение определенного кода.

# while <expression(условие)>
#     <body>
# <else>         не обязательно
#     <body>

# i = 1
# while i <= 10:
#     print(f'Цикл выполнился {i} раз ')
#     i += 1
# else:
#     print('Конец цикла')

# print('Начало кода')

# name1 = ''
# name2 = ''
# i = 0

# while name1.lower() != 'john' and name2.lower() != 'jamie':
#     name1 = input('Введите имя 1: ')
#     name2 = input('Введите имя 2: ')
#     i += 1
#     if i > 4:
#         print('Цикл остановлен! ')
#         break
# else:
#         print('Вы ввели правильное имя! ')

# admin = ['johnsnow23', 'ilovepython23']
# i = 3

# username = None
# password = None

# while username != admin[0] or password != admin[1]:
#     username = input('Enter username: ')
#     password = input('Enter password: ')
#     i -= 1
#     if i == 0:
#         print('Вы заблокированы на 5 минут!')
#         break
# else:
#     print(f'{admin[0]}, Вы успешно зашли в систему! ')

# -------------------------------

# for <variable> in <iterable object>
    # body 

# list_ = [0, 1, 2, 3, 4, 5]
# i = iter(list_)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# for x in list_:
#     print(x)

# --------------------------

# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# for x in ls:
#     print(f'Element: {x}')

# i = 0
# while i < len(ls):
#     print(f'Element: {ls[i]}')
#     i += 1


# secret_list = ['DeltaViski', 'LOTR123', 'JohnSnow']
# word = input('Введите Secret Code: ')
# while word not in secret_list:
#     print('Incorrect word! Try one more time! ')
#     word = input('Введите Secret Code: ')

# print(f'You\'re welcome my friend, {word}!')


# ------------------------------------------------------
# # 1)
# steps = 0
# path = 'UDDDUDUU'
# # result = 1
# sea_level = 0
# dolins = 0

# for x in path:
#     if x == 'U':
#         sea_level += 1
#         if sea_level == 0:
#             dolins += 1
#     elif x == 'D':
#         sea_level -= 1
    
# print(dolins)
# # 2)

# steps = 9
# path = 'UDDUUDDUU'
# dolins = 0
# sea_level = 0

# for x in path:
#     if x == 'U':
#         sea_level += 1
#         if sea_level == 0:
#             dolins += 1
#     elif x == 'D':
#         sea_level -= 1

# print(dolins)







