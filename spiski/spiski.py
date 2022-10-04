# list -> список, массив - изменяемый последовательный тип данных, который предствляет из себя коллекцию каких-либо объектов















# ls = list(range(1, 101))

# for num in ls:
#     if num % 2 == 0:
#         print(f'Число {num} четное, квадрат: {num ** 2}')
#     else:
#         print(f'Число {num} нечетное, куб: {num ** 3}')
    
# Методы списков:

# print(dir([]))

# append(element) -> добавляет элемент в конец списка

# ls = [1, 2, 3]
# print(ls)
# ls.append(5)
# ls.append([6, 7, 8])
# print(ls)
# ls.append(True)
# print(ls)

# extend(iterable) -> расширяет список элементами из iterable object

# ls = [1, 2, 3]
# ls.append('Hello')
# print(ls)
# ls.extend('Hello')
# print(ls)

# ls = [1, 2, 3]
# ls.append([4, 5, 6])
# print(ls)
# ls.extend([4, 5, 6])
# print(ls)

# insert(<index>, <element>) -> добавляет элемент по указанному индексу

# ls = ['string', 2, 3, False]
# ls.insert(1, 4)
# print(ls)
# ls.insert(15, [1, 2 ,3])
# print(ls)

# index(element, [start], [end]) - возвращает индекс элеиента в списке

# ls = ['Hello', 'world', 'my', 'name', 'is', 'John']
# # res = ls.index('name')
# # print(res)
# # print(ls[res])

# print(ls[0:2])
# print(ls[-1][0])


# count(element) -> возвращает кол-во вхождений элемента в списке

# ls = [1, 2, 3, 4, 5, 6, 5, 5, 5]
# res = ls.count(5)
# print(res)

# ls = ['Hello', 'world', 'my', 'name', 'is', 'John', 'north', 'king', 'queen', 'usa']
# print(ls)
# str1 = input('Vvedite slovo: ')
# if str1 in ls:
#     print(f'{str1} есть в списке и его индекс: {ls.index(str1)}')
# else:
#     print('Net!')


# sort() -> сортирует списки, если в аргументах передать reverse=True, то список будет отсортирован в убывающем порядке

# import random

# ls = []
# for x in range(0, 50):
#     ls.append(random.randint(0, 1000))
    
# print(ls)
# ls.sort(reverse=True)
# print()
# print(ls)


# ls = ['John', 'Deyneris', 'Tirion', 'apple', 'Aikol', 'Nurayim', 'makers']
# ls.sort(key=len)
# print(ls)

# remove(element) -> удаляет элемент из списка, а если такого нет - выводится ошибка
# pop([index]) -> удаляет и возвращает элемент по индексу, но если индекс не указан, то удаляет посдений элемент

# ls = [5, 1, 2, 4, 5, 5, 5,]
# # ls.remove(5)
# print(ls)
# while 5 in ls:
#     ls.remove(5)

# print(ls)


# ls = [5, 1, 2, 4, 5, 5, 5, 99]
# delited = ls.pop()
# print(ls)
# print(delited)

# # update --------
# ls = [1, 'h', 3]
# print(ls)
# ls[1] = 2
# print(ls)

