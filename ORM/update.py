from models import Product, Category

# query = Product.update(price=1000000).where(Product.title=='ZARA t_shirt')
# print(query, '!!!')
# query.execute()

# query = Product.update(price=(Product.price + Product.price * 0.5))
# query.execute() #увеличиваем всем товарам цену

# удаление данных
# product = Product.get(Product.title=='ZARA t_shirt')
# print(product)
# print(product.title)
# print(product.category_id.name)
# product.delete_instance()

# query = Product.delete().where(Product.id == 2)
# query.execute()

# category = Category.get(category_id = 3)
# print(category)
# print(category.name)
# category.delete_instance()
