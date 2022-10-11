# dict() - словарь -> упорядочная коллекция элементов (python3.7 -> ordered). 
# Каждый элемент в словаре хранится в виде пары: {ключ: значение}.

# Ассоциативный массив. Hesh tables, objects(JS), structure == dictionary(PY)

# Ключами могут выступать только неизменяемые типы данных и в словаре хранятся уникальные ключи.
# Тогда как значениями могут выступать любые типы данных.

# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1967
# }
# ->
# print(thisdict)
# print(type(thisdict))
# print(thisdict['model'])
# print(thisdict['year'])


# a = dict()
# # b = {1, 2} -> set(множество)
# b = {}
# c = set()
# print(a, b)
# print(type(a))
# print(type(b))
# print(type(c))


# ls = [('key1', 'value1'), ('key2', 'value2') ]
# dict_ = dict(ls)
# print(dict_)

# ----------------------------------------------

# print(dir(dict))

# items, keys, values

# user_info = {
#     'first_name': 'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow@gmail.com',
#     'role': 'admin'
# }
# print(user_info.items())
# print()
# print(user_info.keys())
# print()
# print(user_info.values())

# for value in user_info.values():
#     print(value)

# print(user_info)
# for key, value in user_info.items():
#     print(f'key: {key}, value: {value}')

# ls = list(user_info.items())     -> по индексам
# print(ls[0])


# Изменения элементов в словаре

# dict_ = {'name': 'Jack', 'age': 24}

# print(dict_['name'])
# dict_['name'] = 'John'
# dict_['adress'] = 'WinterFell'
# print(dict_)

# dict_.update({'name': 'John', 'adress': 'WinterFell'})
# print(dict_)

# ---------------------------------

# Создание - fromkeys

# dict_ = {}
# ls = list(range(1, 101))
# new_dict = dict_.fromkeys(ls, 'Value')
# print(new_dict)

# get

# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_.get(2))
# print(dict_[2])
# Burger


# setdefault - работает также как и get, но если нет такого ключа, то он создает новую пару значений из этого ключа

# dict_ = {'name': 'Eddard', 'last_name': 'Stark'}
# print(dict_.setdefault('name'))
# print(dict_.setdefault('age', 38))
# print(dict_)

# Удаление элементов
# pop, popitem

# pop(<key>) - удаляет пару по ключу

# dict_ = {'name': 'John', 'last_name': 'Snow'}
# removed = dict_.pop('adress', 'Такого ключа нет!')
# print(dict_)
# print(removed)

# popitem - удаляет ПОСЛЕДНЮЮ пару
# dict_ = {'name': 'John', 'last_name': 'Snow'}
# removed = dict_.popitem()
# print(dict_)
# print(removed)

# a = {'a': 1, 'b': 2, 'c': 1}
# dict_keys = a.keys()
# print(dict_keys)


# a = {'a': 1, 'b': 2, 'v': 1}
# print(a.keys())


# a = {'a': 1, 'b': 2, 'c': 1}
# print(a.items())
# for x, z in a.items():
#     print(x, z)

# a = {'x': 1, 'y': 2, 'z': 1}
# print(a['x'])

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = {}
# for x in a:
#     if x % 2 == 0:
        
#         print(x)

# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# for res in tuples:
#     if len(res) >= 1:
#         print(list(res))
# print(dir(tuples))

# names = []
# for x in range(0, 5):
#     name = input('Vvedite FIO: ')
#     names.append(name)

# result = []
# for x in names:
#     x = x.split(' ')
#     print(x)
#     result.append(x[-1])

# result.sort()
# print(result)

# # names = []
# # name = [
# #     input(),
# #     input(),
# #     input(),
# #     input(),
# #     input()
# # ]
# # for x in name:
# #     names.append(name)

# # result = []
# # for x in names:
# #     x = x.split(' ')
# #     result.append(x[-1])

# # result.sort()
# # print(result)

# list_ = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# new_list = []
# for x in list_:
#     if type(x) == int:
#         new_list.append(x)
#     elif type(x) == float:
#         new_list.append(x)
        
# print(new_list)
# res = new_list[0] + new_list[1] + new_list[2] + new_list[3] + new_list[4] + new_list[5] + new_list[6] + new_list[7]
# print(res)
# print(sum(new_list))

# list_ = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# new_list = []
# for x in list_:
#     if type(x) == int and x > 0:
#         new_list.append(x)

# res = new_list[0] + new_list[1] + new_list[2] + new_list[3] + new_list[4]
# print(res)

# str_list = ['abc', 'xyz', 'aba', '1221']
# indexs = []
# for x in str_list:
#     if x[0] == x[-1]:
#         indexs.append(str_list.index(x))

# print(indexs)
# list2 = []
# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# list2.append(list_[0::3])
# list2.append(list_[1::3])
# list2.append(list_[2::3])
# print(list2)

# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]
# for x in list1:
#     for y in list2:
#         if x == y:
#             print(True)
#         else:
#             print(False)

# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
# repeats = 3
# res = []
# for x in list_:
#     if list_.count(x) >= repeats:
#         res.append(x)

# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# for ls in colors:

# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# if sum(lists[0]) > sum(lists[1])and sum(lists[2]) and sum(lists[3]):
#     print(lists[0])
# elif sum(lists[1]) > sum(lists[0]) and sum(lists[2]) and sum(lists[3]):
#     print(lists[1])
# elif sum(lists[3]) > sum(lists[0]) and sum(lists[1]) and sum(lists[2]):
#     print(lists[3])
# else:
#     print(lists[2])

# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# a = (
#     input('merge_from = ')
#     input('merge_to = ')
# )
# for res in a:
    

