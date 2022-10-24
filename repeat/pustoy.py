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

# def get_type(a, b):
#     result = type(a), type(b)
#     return result
    
# print(get_type(5, 's'))

# def dictionary():
#     for element in a:
#         print(element)

# print(dictionary('s'))

# num = 6

# def check(num):
#     if num % 2 != 0:
#         print('It is odd number')
#     else:
#         print('It is even number')
    
# print(check(num))

# def is_palindrome(a):
#     if a.lower() == a.lower()[::-1]:
#         return True
#     else:
#         return False
    
# print(is_palindrome('довод'))

# def max_num(a, b):
#     a = input()
#     b = input()
#     return max(a, b)

# print(max_num(10, 12))

# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# new_list = [[x for x in list_[::step]], [y for y in list_[1::step]], [z for z in list_[2::step]]]
# print(new_list)

# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# colors2 = []
# for i in colors:
#     i = i[::-1]
#     colors2.append(i)
# print(sorted(colors2, key = len))

# list_ = [1,2,3,4,5,6,7,8,9,0]
# step = 2
# element = 'a'
# for i in list_[2::step]:
#     list_.remove(i)
#     list_.insert(element, step)
# print(list_)

# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# if sum(lists[0]) > sum(lists[1]) and sum(lists[0]) > sum(lists[2]) and sum(lists[0]) > sum(lists[3]):
#     print(lists[0])
# elif sum(lists[1]) > sum(lists[0]) and sum(lists[1]) > sum(lists[2]) and sum(lists[1]) > sum(lists[3]):
#     print(lists[1])
# elif sum(lists[2]) > sum(lists[0]) and sum(lists[2]) > sum(lists[1]) and sum(lists[2]) > sum(lists[3]):
#     print(lists[2])
# else:
#     print(lists[3])

# list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# repeated = []
# for x in list_:
#     if list_.count(x) >= 2:
#         repeated.append(x)

# print(set(repeated))

# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# cleared_tuples = []
# for x in tuples:
#     if x != ():
#         cleared_tuples.append(x)

# print(cleared_tuples)

# x = 'Я глобальная переменная!'

# def my_func():
#     x = 'Я могу изменяться'
#     print(x)
# print(x)
# my_func()


