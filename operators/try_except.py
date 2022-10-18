# Обработка исключений
# Операторы try.....except

# Ошибки Errors -> связаны с кодом:
#     SyntaxError
#     IdentationError
#     TabError
# и т.д

# Исключения Exceptions -> связаны с неправильными данными, которые передаются в код.
# ZeroDivisionError
# ArithmeticError
# NameError
# IndexError
# KeyError
# ValueError
# ImportError
# BaseException - прородитель исключений

# try:
#     num = int(input('Enter the number: '))
#     print(num)
#     num2 = int(input('Enter the number 2: '))
#     print(num2)
#     print(num / num2)
# except:
#     print('Неправильные данные!')
# print('Очень важная строчка кода!')

# try ... except
# try:
#     <body try>
# except:
#     <body except> сработает, если ошибка в try
# -----------
# <else:>
#     <body else> сработает, если в операторе try нет ошибки

# Не
    # обязательные

# <finally:>
#     <body finally> сработает в любом случае / исходе
# ------------

# try:
#     num1 = int(input('Enter the number: '))
# except:
#     print('Invalid values!')
# else:
#     print(num1)
#     print(num1 + 5)
# finally:
#     print('Код закончился!')


# Отображение ошибки

# 1. import sys
# list_ = [1, 2, 3, 4, 5]
# index = int(input('Enter index: '))
# try:
#     res =  list_[index]
#     print(res)
# except:
#     import sys
#     print(f'Oops, we catched {sys.exc_info()[0]} error!')

# 2. Exception as e / (error)

# ls = [1, 2, 3, 4, 5]
# while True:
#     try:
#         index = int(input('Enter index: '))
#         print(ls[index])
#     except Exception as e:
#         print(f'Oops, we catched {e.__class__} error!')

# try:
#     num1 = int(input('Введите число 1: '))
#     print(num1 / 0)
# except (ValueError, ZeroDivisionError):
#     print('Вы ввели некорректные данные!')

# try:
#     num1 = int(input('Введите число 1: '))
#     print(num1 / 0)
# except ValueError:
#     print('Invalid Values!')
# except ZeroDivisionError:
#     print('Divide by 0!')

# try:
#     num1 = int(input('Enter: '))
#     num2 = int(input('Enter: '))
#     result = num1 / num2
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# except ValueError:
#     print('Invalid Symbols!')
# else:
#     print(result)
# finally:
#     print('The End!')

# -------------------------------------------

# from string import digits

# flag = True
# symbols = digits + '-' + '.'

# while flag:
#     num1 = input('Введите первое число: ')
#     num2 = input('Введите второе число: ')

#     try:
#         num1 = float(num2) if '.' in num1 else int(num1)
#         num2 = float(num2) if '.' in num2 else int(num2)
#     except ValueError:
#         print('Вы ввели неправильное число!')
#         continue
    
#     operator = input('Введите оператор (+, -, *, /): ')
    
#     if operator == '+': 
#         print(f'Результат: {num1 + num2}')
#     elif operator == '-':
#         print(f'Результат: {num1 - num2}')
#     elif operator == '*':
#         print(f'Результат: {num1 * num2}')
#     elif operator == '/':
#         if num2 == 0:
#             print('На ноль делить нельзя!')
#         else:
#             print(f'Результат: {num1 / num2}')
#     else:
#         print('Вы ввели неправильный оператор!')

#     choice = input('Хотите остановить?(yes): ')
#     if choice.lower() == 'yes':
#         flag = False
#         print('Пока!')

# n = int(input('Enter number 1-100: '))
# # dict_ = {num: x if x % n == 0 }
# dict_ = {x in range(1, 501): x ** 2 for x in n}
# print(dict_)

# dict_ = {'first': 1, 'second': 2, 'third': 3}
# a = {'even' if x % 2 == 0 else 'odd' for x in dict_.values()}
# print(a)

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [x for x in string_ if x]
# print(list_)

# num1 = int(input())
# num2 = int(input())

# try:
#     print(num1 + num2)
# except ValueError:
#     print('Введите число!')

# try:
#     num1 = int(input('Enter: '))
#     num2 = int(input('Enter: '))
#     result = num1 + num2
# except ValueError:
#     print('RURURU')
# else: print(result)

# try:
#     age = int(input())

# except ValueError:
#     print('Доступ запрещён')
# except:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')

# try:
#     cash = int(input())
# except ValueError:
#         print('Сумма не может быть отрицательной!')
# else:
#     print(cash)

a = {1, 1, 1, 1, 1}
