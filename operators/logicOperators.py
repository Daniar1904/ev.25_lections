# Операторы сравнения
# Условные операторы
# Логические операторы

# Операторы сравнения 
# <, >, ==(равно), <=, >=, !=(не равно)

# 1 < 5 -> true
# 7 > 9 -> false 
# num1 = 18
# num2 = 15
# print(num1 <= num2)

# num1 = 20
# num2 = 17
# print(num1 != num2)

# stroka1 = 'hello'
# stroka2 = 'world'
# print(stroka1 < stroka2)
    #    72       87

# print('Hello world')
# print(ord('H'))        -> в ascii code
# print(ord('а')) - русский

# print(chr(1080)) ->      обратно
# print(chr(1080), chr(1089))
# print(ord('И'))

# stroka1 = 'Hello!'
# stroka2 = 'World John Snow'
# print(len(stroka1) > len(stroka2))


# Условные операторы
# if
# elif
# else

# if <condition>:
#     <body if> 
#     #  сработает если в вырадении if придет True
# [elif] <condition>:
#        <body if>
# [else]:
#     <body esle> 
    # срабатывает если во всех вышестоящих условиях пришло False

# string = input('Enter smt:')
# if string.lower() == 'hello':
#     print('Hello stranger')
# elif string.lower() == 'john':
#     print('Welcome back John Snow! The king of North!')
# elif string.lower() == 'abra-Kadabra':
#     print('Sim Salamon Kadabra!')
# else:
#     print('Совпадений не найдено!')


# email = input('Enter email:')
# password1 =  input('Enter the password:')

# if len(password1) < 8:
#     raise ValueError('Password too short!')

# password2 = input('Enter the password confirmation:')
# if password2 != password1:
#     raise ValueError('Password didn\'t match!')
# else:
#     print('Successfully signed up!')


# age = input('Enter your age:')

# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('Invalid Values!')

# if age < 18:
#     print(f'Access Denied! Come again after {18 - age} age!')
# else:
#     print('You can buy it!')


# Логические операторы
# and -> логическое и 
# or -> логическое или
# not -> логическое отрицание

# my_age = 20
# your_age = 18
# result = my_age == 20 and your_age == 19
# print(result)

# my_age = 20
# your_age = 18
# result = my_age == 21 or your_age == 19
# print(result)

# my_age = 20
# your_age = 18
# result = not my_age == 21 and not your_age == 19
# print(result)

# name = input()
# surname = input()
# age = input()
# res = (f'Меня зовут {name} {surname}, Мой возраст: {age}')
# print(res)

# ---------------------------------------

# user = 'John'
# is_google_user = True
# is_github_user = False
# is_age_greater_21 = False
# user_coins = 9000

# # либо user google или  github, либо 21, либо бабки(8000)
# if (is_google_user or is_github_user) and (is_age_greater_21 or user_coins > 8000):
#     print(f'You can enter the system, Mr/Mrs {user}!')
# else:
#     print('Sorry, you couldn\'t enter!')

# Операторы идентификации
# in -> проверяет наличие элементов какого-либо интерируемого объекта(строки, строки  и т.д.)
# is -> сравнировает ячейки памяти двух объектов
    #  == -> сравнивает по значению
# is not -> отрицательное сравнение ячеек памяти

# str1 = 'Hello world'
# print(str1)
# choice = input('Enter the symbol:')

# if choice in str1:
#     print(f'The symbol: {choice} exist!')
# else:
#     print(f'The symbol: {choice} does not exist!')



