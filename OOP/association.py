# Ассоциация, Композиция, Агрегация
# Все эти три принципа очень похожи друг на друга. Все они означают, что внутри одного объекта будет существовать другой объект.

# Композиция
# class Wall:
#     def init(self, direction) -> None:
#         self.type = direction

#     def str(self) -> str:
#         return f'{self.type}'

# class Room:
#     def init(self) -> None:
#         self.west_wall = Wall('west')
#         self.east_wall = Wall('east')
#         self.south_wall = Wall('south')


# class Logger:
#     def init(self) -> None:
#         self.stream = None

#     def print_the_stream(self):
#         if self.stream:
#             print(f'Stream from class: {self.stream}')
#         else:
#             print(f'None stream!')

# stream = Logger()
# stream.print_the_stream()
# stream.stream = Stream()
# stream.print_the_stream()

# Агрегация

# class Stream:
#     def str(self) -> str:
#         return 'Stream object!'

# class Logger:
#     def init(self, stream =None) -> None:
#         self.stream = stream

#     def print_the_stream(self):
#         if self.stream:
#             print(f'Stream from class: {self.stream}')
#         else:
#             print(f'None stream!')

# stream = Stream()
# logger = Logger(stream)
# logger.print_the_stream()

# class Engine:
#     country = 'Germany'

#     def init(self, power) -> None:
#         self.power = power

#     def str(self):
#         return f'Power: {self.power}'

# class AudiCar:
#     brand = 'Audi'
#     country = 'Germany'

#     def init(self, model, power) -> None:
#         self.engine = Engine(power)
#         self.model = model

#     def str(self) -> str:
#         return f'{self.brand} {self.model} -> {self.engine} -> engine country: {self.engine.country}. Country of car: {self.country}'

# car = AudiCar('A8', 600)
# print(car)