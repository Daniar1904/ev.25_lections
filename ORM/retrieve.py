import peewee
from models import Product, Category

# def get_all_categories():
#     return Category.select()

# def get_all_products():
#     return Product.select()

# categories = get_all_categories()
# # print(categories, '!!!!')
# print('КАТЕГОРИИ В БД')
# for x in categories:
#     print(x, x.name)

# products = get_all_products()
# print('ВСЕ ПРОДУКТЫ В БД')
# for x in products:
#     print(x, x.title, x.price, x.category_id)

# category_jeans = Category.get(Category.name == 'джинсы')
# print(category_jeans)
# print(category_jeans.name)

# for product in category_jeans.products: #related name
#     print(f'Title: {product.title}, Price: {product.price}, Category: {product.category_id.name}')

