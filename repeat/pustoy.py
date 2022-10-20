# list_ = ['Marat', 'Samat', 'Turat', 'Jyrgalbek', 'Timur']
# for name in list_:n
#     print(name)

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for list1 in list_:
#     if list1 % 2 == 0:
#         print(list1)
    
# for list2 in list_:
#     if list2 % 2 != 0:
#         print(list2)

# list1 = [1, 345, 124]
# list2 = [8, 321, 6]
# x = list1[0] + list1[1] + list1[2]
# y = list2[0] + list2[1] + list2[2]
# res = x + y
# print(res)

# year = int(input('Enter year: '))
# if year % 4 == 0 and year % 100 != 0:
#     print('YES')
# elif year % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for list1 in list_:
#     if list1 % 2 == 0:
#         print(list1)
# print()
# for list2 in list_:
#     if list2 % 2 != 0:
#         print(list2)

# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# lisr_ = str(list_)
# letter = input('Enter first letter: ')
# for ls in list_:
#   if letter == ls[0]:
#     print(ls)

# a = {100, 90, 3, 4}
# b = {3, 4, 5, 6}
# c = a.union(b)
# print(c)
# # res = {}
# for x in a:
#     for y in b:
#         if x == y:
#             res  = set(res)
#             res.add(x)

# print(res)

# a = {1, 2, 3}
# b = {5, 6, 3, 2, 7, 1}
# if len(a) < len(b):
#     print('Подмножество!')

# a = {1, 2, 3}
# b = {5, 6, 3, 2, 7, 1}
# if len(b) > len(a):
#     print('Надмножество!')

# robert = {5, 7, 11, 10, 28} 
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 11, 10}
# for x in robert:
#     for y in kail:
#         for z in merri:
#             if y != x and z != x:
#                 print('no one')
#             else:
#                 print('kail merri')

# str_ = 'rf 5 gvrfcw 46534'
# list_ = []
# for x in str_:
#     if x.isdigit():
#         list_.append(x)

# print(list_)

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [x for x in string_ if x.isnumeric()]
# print(list_)
# num_list = []

# num = ''
# for x in string_:
#     if x.isdigit():
#         num = num + x
#     else:
#         if num != '':
#             num_list.append(int(num))
#             num = ''

# if num != '':
#     num_list.append(int(num))

# print(num_list)

# num_list = [num + x for x in string_ if x.isdigit() else num != '']
# num_list = [x for x in string_ if x.isdigit()]
# print(num_list)

# dict_ = {'key1': 'value1', 'key2': 'value2'}
# try:
#     print(dict_['key3'])
# except KeyError:
#     print('Нет такого ключа!')

# try:
#     age = int(input())
#     result = (x for x in age if x >= 18)
#     # print(result)
# except ValueError:
#     print('Доступ запрещён')
# except:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')





