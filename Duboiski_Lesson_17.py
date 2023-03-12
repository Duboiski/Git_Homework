# ДЗ на вторник:
# 1. Создайте класс Person, который имеет атрибуты name и age, а также метод greet()
# (выводит приветствие на экран с именем персоны).
# 2. Создайте класс Car, который имеет атрибуты make, model и year, а также
# метод get_info() (возвращает строку, содержащую информацию о машине).

class Person:
    name = ''
    age = 1950
    def greet(self):
        print(f'Мы рады вас видеть {self.name}!\n')

class Car:
    make = 'Lada'
    model = 'XRay'
    year = 2019
    def get_info(self):
        print('Вы выбрали автомобиль: ')
        print(f'    Производитель: {self.make}')
        print(f'    Модель: {self.model}')
        print(f'    Год выпуска: {self.year}')

print('Задание 1')
a = Person()
a.name = input('Как вас завут? ')
a.greet()

print('Задание 2')
x = Car()
n = int(input('Выбирите автомобиль (1 - по умолчанию, 2- ввести самостоятельно): '))
if n == 1 :
    x.get_info()
if n == 2:
    x.make = input('Введите производителя автомобиля: ')
    x.model = input('Введите модель автомобиля: ')
    x.year = input('Введите год выпуска автомобиля: ')
    x.get_info()


