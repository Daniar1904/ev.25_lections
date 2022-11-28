# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число). 
# Протестируем функцию на файле «article.txt» со следующим содержимым:

# def read_lines(lines, file):
#     if lines > 0:
#         with open('article.txt', 'r') as file:
#             data = file.readlines()[::-1]
#             for i in range(0, lines):
#                 try:
#                     print(data[i].strip())
#                 except IndexError:
#                     print('Строки закончились!')
#                     break
#     else:
#         print('Количество строк должно быть положительным!')

# read_lines(3, 'article.txt')
# read_lines(-4, 'article.txt')
# read_lines(30, 'article.txt')


# Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
# – № - номер по порядку (от 1 до 300);
# – Секунда – текущая секунда на вашем ПК;
# –  Микросекунда – текущая миллисекунда на часах.
# На каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
        
# import csv
# from datetime import datetime
# from time import sleep

# with open('rows_300.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['№', 'Hours', 'Minutes', 'Seconds', 'Microseconds'])
#     for x in range(1, 301):
#         print(x)
#         hours = datetime.now().hour
#         minutes = datetime.now().minute
#         seconds = datetime.now().second
#         microseconds = datetime.now().microsecond
#         writer.writerow([x, hours, minutes, seconds, microseconds])
#         sleep(0.01)


# 1. У нас есть файл file.txt c текстом на латинице. Нужно написать программу, которая будет выводить статистику по тексту:

#     > количество букв латинского алфавита
#     > число слов
#     > число строк

# with open('file.txt', 'r') as file:
#     data = file.read()
#     letters = sum(map(str.isalpha, data))
#     words = len(data.split())
#     file.seek(0)
#     lines1 = len(file.readlines())
#     lines2 = data.count('\n') + 1
#     print('Input files contains!')
#     print(f'{letters} - letters!')
#     print(f'{words} - words!')
#     print(f'{lines1} - lines!')



# """Напишите программу, которая получает на вход строку с названием текстового файла, и выводит на экран содержимое этого файла, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл forbidden_words.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
# """

# Input: "Hello, world! Python IS the programming language of thE future. My EMAIL is....
# PYTHON is awesome!!!!"

# Output: *, *ld! ****  * programming language of * future. My *** **....
# ** ** awesome!!!!

# with open('forbidden_words.txt') as forbidden_file, open('input.txt') as text_file:
#     forbidden_words = forbidden_file.read().split(' ')
#     text = text_file.read()
#     text_lower = text.lower()
#     for word in forbidden_words:
#         text_lower = text_lower.replace(word, '*' * len(word))
        
#     result = [x if x == '*' else y for x, y in zip(text_lower, text)]
#     result = [(y, x)[x == '*'] for x, y in zip(text_lower, text)]
#     print(''.join(result))


# """
# 1) Откройте файл task5.txt. В нём записаны целые числа. Прочтите эти числа, затем найдите максимальное затем минимальное число. Затем запишите эти числа в новый файл task6.txt через символ - (сначала минимальное, потом максимальное)
# """

# with open('task5.txt', 'r') as file:
#     res = []
#     for i in file.read():
#         if i.isdigit():
#             res.append(i)
#     with open('task6.txt', 'w') as file:
#         file.write(f'{min(res)} - {max(res)}')


# 2) Расчет премии сотрудникам
# # salary- это заработная плата в месяц, overTime- количество часов, которое сотрудник взял сверхурочно, задача: создать функцию, которая будет добавлять к основной зарплате сверхурочное время(1час=200$), функция должна принимать список со словарями и возвращать также список, но уже с измененными данными пример: [{'name': 'Jack', 'salary': 10000, 'overTime': 4}] -> [{'name': 'Jack', 'salary': 10800}]

# employees = [
#     {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]
# res = []
# for i in employees:
#     name = i['name']
#     salary = i['salary']
#     overtime = i['overTime']
#     salary += overtime * 200
#     res.append({'name': name, 'salary': salary})
# print(res)


# Даны три переменные a, b и c. Изменить значения этих переменных так, чтобы в a хранилось значение a+b, в b хранилась разность старых значений c− b, а в c хранилось сумма старых значений a+b+c.
# Пример: a=0, b=2, c=5, тогда новые значения a=2, b=3 и c=7.
# a = 0
# b = 2
# c = 5
# a, b, c = a + b, c - b, a + b + c
# print(a, b, c)


# Написать функцию, которая выводит периметр, площадь и диагональ квадрата, после того как пользователь вводит сторону.
# from math import sqrt
# def func(a):
#     p = a * 4
#     s = a ** 2
#     d = a * sqrt(2)
#     return p, s, d

# print(func(4))


# Дано четырехзначное число. Поменяйте местами наименьшую и наибольшую цифры.
# Пример: 1234 => 4231

# a = 1234
# ref = list(str(a))
# min_num = min(ref)
# max_num = max(ref)
# idx1 = ref.index(min_num)
# idx2 = ref.index(max_num)
# ref[idx1] = max_num
# ref[idx2] = min_num
# print(int(''.join(ref)))

# Напишите программу, которая проходиться по числам в диапазоне от 1 до 50. Вывести “Fizz”  для чисел в этом диапазоне, которые кратны 3, вывести “Buzz” для чисел, которые кратны 5 и вывести “FizzBuzz” для чисел которые делятся и на 3 и на 5.
# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
    

# Вывести все пятизначные числа, которые делятся на 2, у которых средняя цифра нечетная, и сумма всех цифр делится на 4.
# Пример: 33541, 73541 и тд.
# res = []
# for i in range(10000, 10150):
#     mid = len(str(i)) // 2
#     if i % 2 == 0 and int(str(i)[mid]) % 2 != 0 and sum([int(i) for i in str(i)]):
#         res.append(i)
# print(res)


# Дан список с визитами по городам и странам. Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России. Считайте, что список geo_logs легко помещается в оперативной памяти.
# geo_logs = [{"visit2": ["Дели", "Индия"]}, {"visit3": ["Владимир", "Россия"]}, {"visit9": [“Курск", “Россия"]}]
# geo_logs = [{"visit2": ["Дели", "Индия"]}, {"visit3": ["Владимир", "Россия"]}, {"visit9": ["Курск", "Россия"]}]
# for i in geo_logs.copy():
#     if not 'Россия' in list(i.values())[0]:
#         geo_logs.remove(i)
# print(geo_logs)


# Дана дата из трех чисел (день, месяц и год). Вывести Yes, если такая дата существует (например, 12.02.1999 => yes, 22.13.2001 => no). Примечание*(Считать количество дней в феврале как 28 дней)
# date_ = '22.13.2001'
# date_2 = '12.02.1999'

# def func(date_):
#     res = []
#     ref = date_.split('.')
#     date = ref[0]
#     month = ref[1]
#     year = ref[-1]
#     if int(month) <= 12:
#         if month not in ['02', '04', '09']:
#             if int(date) in range(1, 32):
#                 res.append(True)
#             else:
#                 res.append(False)
#         elif month == '04' or month == '09':
#             if int(date) in range(1, 31):
#                 res.append(True)
#             else:
#                 res.append(False)
#         elif month == '02':
#             if int(date) in range(1, 29):
#                 res.append(True)
#             else:
#                 res.append(False)    
#     else:
#         res.append(False)
#     if year != '0':
#         res.append(True)
#     else:
#         res.append(False)
#     return 'Yes' if all(res) else 'No'

# print(func(date_)) # No
# print(func(date_2)) # Yes

class Taxi:
    def __init__(self, name, cost, cost_km) -> None:
        self.name = name
        self.cost = cost
        self.cost_km = cost_km
    
    def get_total_cost(self, km):
        self.km = km
        return self.cost * self.km

namba
        

