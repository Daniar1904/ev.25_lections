# Class Methods, instance methods, static methods

# Методы экземпляра(объекта) класса (instance methods) - это те методы в ООП, которые изменяют состояние объекта от класса.
    # def method(self) - self это ссылка на объект

# Методы класса (class methods) - это те методы, которые могут изменять состояние самого класса и манипулировать им.
    # @classmethod
    # def method(cls) - cls это ссылка на сам класс

# Статические методы(static methods) - это те методы которые не могут изменять состояние ни объекта, ни самого класса.
    # @staticmethod
    # def method()

# class Student:
#     school_name = 'Sibat'
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def show(self):
#         print(self.name, self.age, 'School:', Student.school_name)

#     @classmethod
#     def change_school(cls, name):
#         # print(cls, '!!!!')
#         cls.school_name = name

# obj = Student('John Snow', 20)
# obj.show()
# obj.change_school('ABC school')
# obj.show()
