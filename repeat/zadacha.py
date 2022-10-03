# import random

# ls = ['Plov', 'Manty', 'Kuurdak', 'Lagman', 'Oromo']
# p = 0
# m = 0
# k = 0
# l = 0
# o = 0

# for x in range (0, 100000):
#     # print(x)
#     choice = random.choice(ls)
#     print(choice)
#     if choice.lower() == 'plov':
#         p += 1
#     elif choice.lower() == 'manty':
#         m += 1
#     elif choice.lower() == 'kuurdak':
#         k += 1
#     elif choice.lower() == 'lagman':
#         l += 1
#     else:
#         o += 1
# print('Результаты голодных игр:')
# print(f'Plov: {p}\nManty: {m}\nKuurdak: {k}\nLagman: {l}\nOromo: {o}' )

# print("Ноль в качестве знака операции"
#       "\nзавершит работу программы")
# while True:
#     s = input("Знак (+,-,*,/): ")
#     if s == '0':
#         break
#     if s in ('+', '-', '*', '/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if s == '+':
#             print("%.2f" % (x+y))
#         elif s == '-':
#             print("%.2f" % (x-y))
#         elif s == '*':
#             print("%.2f" % (x*y))
#         elif s == '/':
#             if y != 0:
#                 print("%.2f" % (x/y))
#             else:
#                 print("Деление на ноль!")
#     else:
#         print("Неверный знак операции!")


