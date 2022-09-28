# print(dir(str))
#  методы строк
#  replace(old, new, [count]) - меняем в строке old на new значение, если вы укажите count, то он заменит его ровно count раз.

# text = 'ha ha ha ha'
# result = text.replace('a', 'i', 2) 
# print(text)
# print(f'result after replace: {result}')

# str1 = 'Hello world! My name is John Snow'
# result = str1.replace('John Snow', 'Jamie Lanister')
# print(result)

# print(id('H'))
# print(id('H'))
# print(id('h'))

# strip() - убирает пробельные символы в начале и в конце строки
# rstrip, lstrip

# text = input('Enter the text:')
# print(text)
# print(len(text))
# result = text.strip()
# print(result)
# print(len(result))

# text = '   Hello world   '
# print(len(text))
# res = text.lstrip()
# print(res)
# print(len(res))

# print(dir(str))


# isdigit() ->                 Проверяет
# isnumeric() -> ->  состоит ли наша строка полностью 
# isedecimal() ->              из чисел

# text = '57'
# if text.isdigit():
#     num = int(text)
#     print(num)
# else:
#     print('Oops! Invalid symbols!')

# text = '\u0031'
# print(text)
# print(text.isnumeric())


# isalnum() -> проверяет состоит ли наша строка из чисел и символов латинского алфавита и кириллицы.

# str1 = '56a'
# print(str1.isalnum())
# str2 = '56_a'
# print(str2.isalnum())

# isalpha() -> состоит ли наша строка полностью из символов латинского либо кирилльского алфавита

# text = 'Hello world'
# print(text[:5].isalpha())

# islower()
# isupper()
# istitle() -> каждое слово с большой буквы(проверка)

# ----------------------

# index(value, [start], [end]) -> выводит индекс значения value котороее мы передаем в нашей строке 

# text = 'Hello world! My name is John Snow'
# print(text.index('John'))
# res = text.index('o')
# print(res)
# res = (text.index('o', res+1))
# print(res)
# res = (text.index('o', res+1))
# print(res)
# res = (text.index('o', res+1))
# print(res)


# # count(value, [start], -> считает кол-во вхождений value в нашу строку)
# text = 'hello o o hello'
# print(text.count('hello'))
# print(text.count('o'))
# print(text.count(' '))

# как найти все индексы символа 'о'
# # text = 'oooHello world! Myo name is John Snowooo'
# text = input('Enter the text:')
# i = 0
# res = -1
# while i < text.count('o'):
#     # 4 time
#     res = text.index('o', res+1)
#     print(res)
#     i += 1
#     #  i += 1 -> это инкремент


# find(value, [star], [end]) -> делает то же самое что и index, но есть одно отличие. 
# В том, что если value нетв строке, то возвращается индекс -1

# text = 'hello'
# print(text.find('l'))
# print(text.find('hi'))


# swapcase() -> переводит все символы в противоположный регистр
# upper(), lower() - верхний и нижний регистры

# text = 'hellO World, JoHN, SNow'
# print(text)
# print(text.swapcase())
# print(text.upper())
# print(text.lower())

# capitalize() - переводит первую букву в верхний регистр 
# name = input('Enter your name:').capitalize()
# print(f'Hello mr/mrs {name}!')

# title() - переводит первые символы всех слов в верхний регистр 
# text = 'john jamie sansa nursultan jerry'
# print(text.title())
# print(text.capitalize())

# name = input('Vvedite svoe FIO: ')
# print(name.title())

# split(разделитель) - дробит строку на несколько частей по разделителю который находится в строке
# все части строки сохраняются в тип данных -list-

# text = 'Let me speak by my hearth in English! Cause My name is John Snow!'
# ls = text.split(' ')
# print(ls)
# print(len(ls))

# 'Разделитеь=ль'.join(iterable(list)) -> соединяет строки по разделителю строки, которые находятся в list.

res = '#'.join(ls)
print(res)




