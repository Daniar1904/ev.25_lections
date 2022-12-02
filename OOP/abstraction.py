# Абстракция(абстрактный класс) - его можно рассматривать как набор методов, которые обязаны быть созданы и реализованы во всех дочерних классах, которые унаследованы от абстрактного класса.
# Абстрактный метод - это метод, у которого есть объявление, но нет реализации.
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     def __init__(self, name) -> None:
#         self.name = name

#     @abstractmethod
#     def area(self):
#         pass

#     def fact(self):
#         print('я фигура в двумерной плоскости!')

# class Square(Shape):
#     def __init__(self, lenght) -> None:
#         super().__init__('Square')
#         self.length = lenght

#     def area(self):
#         return self.length ** 2

# class Circle(Shape):
#     def init(self, radius) -> None:
#         super().__init__('Окружность')
#         self.radius = radius

#     def area(self):
#         from math import pi
#         return pi * (self.radius ** 2)

# obj1 = Square(6)
# obj2 = Circle(3)
# print(obj1.area())
# print(obj2.area())

# -----------------------------------------

# from abc import ABC, abstractmethod

# class ChessPiece(ABC):
#     # Общий метод, который будут использовать все наследники этого класса
#     def draw(self):
#         print('Drew a chess piece!')

#     # Абстрактный метод, который необходимо переопределить для каждого дочернего класса. 
#     @abstractmethod
#     def move(self):
#         pass

# class Queen(ChessPiece):
#     def move(self):
#         print('Queen can move everywhere: diogonaly, verticaly and gorizontaly!')

# class Pawn(ChessPiece):
#     def move(self):
#         print('Pawn can move directly to one sell!')

# q = Queen()
# p = Pawn()

# q.draw()
# q.move()

# p.draw()
# p.move()

# -------------------------------------------------------------------
