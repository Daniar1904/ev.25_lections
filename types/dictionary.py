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


a = {'a': 1, 'b': 2, 'c': 1}
print(a.items())
for x, z in a.items():
    print(x, z)






