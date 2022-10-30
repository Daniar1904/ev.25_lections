# Работа с файлами

# Каретка - указатель - курсор

# open(<путь до файла>)
# file = open('/Users/daniar/Desktop/ev.25/files/lections/files.py') #абсолютный путь
# file = open('files.py') # относительный путь (относительно к той директории, в которой вы работаете)

# Режимы работы с файлами
# 1. чтения -> r/r+ (read)
# 2. записи -> w/w+ (write)
# 3. добавления -> a/a+ (append)
# b x t

# file = open('test.txt', 'r')
# print(file.read())
# file.close()

# file = open('test.txt', 'r')
# data = file.read()
# data = data.split('\n')
# print(data)
# print(len(data))
# file.close()


# Контекстный менеджер
# with open('test.txt') as file:
#     print(file.tell())
#     data = file.read()
#     index = data.index('My')
#     print(file.tell())
#     file.seek(index)
#     print(file.read())
#     print(file.tell())

# file.tell() -> возвращает индекс: где находится указатель/курсор/каретка
# file.seek(index)-> перемещает каретку на индекс, который вы передали

# with open('test.txt', 'r') as file:
#     print(file.readlines())
#     file.seek(0)
#     print(file.readline())
#     print(file.readline())

# print(file.read()) # Ошибка!!!

# with open('test.txt', 'a+') as file:
#     file.write('\nHe is bastard of Ned Stark')
#     file.write('This is lesson about files\n')
#     file.seek(0)
#     print(file.read())

# with open('test.txt', 'w') as file:
#     file.write('Hello, file was opened with open!')

# brew install tesseract!!!!!!!!!!!!!!

# ----------------------------------------------------

# В терминале  pip3 install pytesseract

# Потом

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import re

def get_imei_codes(list_images):
    for image in list_images:
        string = pytesseract.image_to_string(image)
        # print(string)
        list_of_imei = re.findall(
                r'IMEI\d.\s\d+', string
            )
        print(list_of_imei)

    with open('imei_codes.txt', 'w') as file:
        for x in list_of_imei:
            file.write(f'{x}\n')

ls = ['imei.jpg']
get_imei_codes(ls)

# ДРУГОЙ

# # def get_imei_codes(list_images):
# #     string = pytesseract.image_to_string(image)
# #     # print(string)
# #     list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
# #     print(list_of_imei)

# #     with open('imei_codes.txt', 'w') as file:
# #         for x in list_of_imei:
# #             file.write(f'{x}\n')

# # ls = ['imei.jpg']
# # get_imei_codes(ls)
