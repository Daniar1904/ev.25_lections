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

year = int(input())

result = (
    'YES' if year % 4 == 0 and 
    year % 100 != 0 or 
    year % 400 == 0 else 'NO'
)

print(result)


