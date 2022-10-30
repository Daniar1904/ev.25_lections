# num = 1
# while num >= 0:
#     try:
#         num = int(input('Введите число: '))
#     except ValueError:
#         pass
# else:
#     print('Встретилось отрицательное число!')
    
# ----------------------------------------------

# from random import randint
# ls = []
# for x in range(0, 100):
#     ls.append(randint(1, 50))

# print(ls)
# print()
# ls = list(set(ls))
# result = sorted(ls)
# print(result)

# ----------------------------------------------

# def introduce(name, last_name, wife = 'Холост', **kwargs):
#     print(f'Привет, это {name} {last_name}')
#     print(f'Он {wife}')
#     if kwargs:
#         print(f'Инициалы его жены {" ".join(kwargs.values())}')

# introduce('John', 'Snow')
# introduce('Tirion', 'Lanister', 'Женат', wife_name = 'Sansa', wife_last_name = 'Stark')

# ----------------------------------------------

# roles = {
#     0: 'Admin',
#     1: 'Customer',
#     2: 'Vendor'
#     }

# users = [
#     {
#     'id': 1,
#     'username': 'John',
#     'role': roles[0]
#     },
#     {
#     'id': 3,
#     'username': 'Tirion',
#     'role': roles[2]
#     },
#     {
#         'id': 2,
#         'username': 'Raychel',
#         'role': roles[1]

#     }
#     ]

# product = {
#     'id': 1,
#     'title': 'iPhone 14',
#     'description': 'Lorem Ipsum',
#     'price': 1200
# }
# print(f'Before: {product}')

# id_user = int(input('Введите свой ID: '))
# try:
#     user = list(filter(lambda x: x['id'] == id_user, users))[0]
#     print(f'Welcome, {user}!')
# except IndexError:
#     raise ValueError('Invalid ID for user! User with this ID does not exist!')

# if user['role'] == roles[0]:
#     choice = input('Введите, что изменить: ')
#     product[choice] = input('Введите новое значение: ')
# else:
#     raise Exception('Permition denied!')

# print(f'After: {product}')

# ----------------------------------------------

# period = 3
# min_sum = 30000
# depozit = int(input())
# res = (((depozit * 10) // 100) * period)

# def get_percentage(money, period):
#     if money < 30000:
#         raise Exception('Минимальная ставка - 30000 сомов')
#     if period < 3:
#         raise Exception('Минимальный срок - 3 года')
    
#     i = 0
#     while i < period:
#         money += money * 0.1
#         # money = money * 1.1
#         # money = money + (money / 100 * 10)
#         i += 1
#     return money

# money =  int(input('Введите сумму денег: '))
# year = int(input('Введите срок вашего депозита: '))

# print(get_percentage(money, year))

# ----------------------------------------------

# ls = [[100, 2, 3], [300, 3, 5], [200, 50, 50, 50], [45, 45, 6]]
# def find_max(ls):
#     return max(sum(x) for x in ls)

# print(find_max(ls))

# ----------------------------------------------

# # str1 = 'Hello world! My name is John, last name is Snow. Nice to meet you!'
# def get_reverse_string(text):
#     spisok = text.split()[::-1]
#     return ' '.join(spisok)

# print(get_reverse_string('Hello world ! My name is John, last name is Snow. Nice to meet you !'))
