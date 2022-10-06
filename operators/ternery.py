# sentence = input('Vvedite predlojeniye:')
# if sentence[-1] == '?':
#     print('Predlojeniye voprositelnoye')
# else:
#     print('Obychnoye predlpjeniye')

# sentence = input('Vvedite predlojeniye:')
# print('Предложение вопросительное' if sentence[-1] == '?' else 'обычное предложение')

# ---------------------------------------

# Ternary operator(Тернарный оператор) -> это конструкция котороая аналогична по своим свойствам и действию конструкции if/else, 
# но при этом записывается в одну строчку кода.

# <выражение если в условии True> if <условие> else <выражение если False>

# number = 18
# res = 'even number' if number % 2 == 0 else 'odd number'
# print(res)

# from string import digits 

# symbols = digits + '-'
# print(symbols)
# number = input('Vvedite chislo: ')
# is_correct = True
# for i in number:
#     if i not in symbols:
#         is_correct = False

# if is_correct:
#     print('Yes number!')
#     number = int(number)
#     print('Your number:', number)
#     result = number if number >= 0 else -number

#     print(result)
# else:
#     print('Invalid Values!')

# number = input('Введите число: ')
# if  number.isdigit():
#     number = int(number)
#     print(number)
#     print('Да, число!')
# else:
#     print('Вы ввели не число!')

# ----------------------------------------------------------------------

# from string import digits

# flag = True
# symbols = digits + '-' + '.'

# while flag:
#     is_correct_number = True
#     num1 = input('Введите первое число: ')

#     if len(num1) <= 1 and (num1 == '.' or num1 == '-') or not num1:
#             print('Вы ввели неправильное число!')
#             is_correct_number = False

#     for x in num1:
        
#         if x not in symbols:
#             print('Вы ввели неправильное число!')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue

#     num2 = input('Введите второе число: ')
#     if len(num2) <= 1 and (num2 == '.' or num2 == '-') or not num2:
#             print('Вы ввели неправильное число!')
#             is_correct_number = False

#     for x in num2:
        
#         if x not in symbols:
#             print('Вы ввели неправильное число!')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue

#     num1 = float(num2) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)
#     print(num1)
#     print(num2)
    
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
    