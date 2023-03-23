# Написать программу для учета животных в зоопарке
# В родительском абстрактном классе Animals создать абстрактные методы для любого животного
# От родительского класса наследовать классы для конкретных видов животных
# Также использовать полиморфизм, инкапсуляцию
# При печати объектов определенного класса выводить информацию об этом объекте.
# setter и property можно не использовать!
# print(sinica) #при печати таких объектов должна выводиться информация о них, а не свойства объекта или класса

from abc import ABC, abstractmethod
class Animals(ABC):
    @abstractmethod
    def are_living(self):
        pass

    @abstractmethod
    def are_eating(self):
        pass

    @abstractmethod
    def are_moving(self):
        pass

class Birds(Animals): # птицы
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def are_living(self):
        return 'Живут на деревиях'

    def are_eating(self):
        return 'Питаются семена и насекомых'

    def are_moving(self):
        return 'Передвигаются по воздуху'

    def __str__(self):
        return f'Животное {self.name} возрост {self.age} года'

    def _areal(self):
        return self.are_living() + '\n' + self.are_eating() + '\n' + self.are_moving()

class Monkey(Animals): # обезьяны
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def are_living(self):
        return 'Живут на деревиях'

    def are_eating(self):
        return 'Питаются фруктами и насекомых'

    def are_moving(self):
        return 'Передвигаются по деревьям'

    def __str__(self):
        return f'Животное {self.name} возрост {self.age} года'

    def _areal(self):
        return self.are_living() + '\n' + self.are_eating() + '\n' + self.are_moving()

class Feline(Animals): # кошачие
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def are_living(self):
        return 'Живут на земьле'

    def are_eating(self):
        return 'Питаются мясом'

    def are_moving(self):
        return 'Передвигаются по земле'

    def __str__(self):
        return f'Животное {self.name} возрост {self.age} года'

    def _areal(self):
        return self.are_living() + '\n' + self.are_eating() + '\n' + self.are_moving()

class Fish(Animals): # рыбы
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def are_living(self):
        return 'Живут в воде'

    def are_eating(self):
        return 'Питаются насикомыми и растениями'

    def are_moving(self):
        return 'Передвигаются в воде'

    def __str__(self):
        return f'Животное {self.name} возрост {self.age} года'

    def _areal(self):
        return self.are_living() + '\n' + self.are_eating() + '\n' + self.are_moving()

cockatoo = Birds('Какаду', 2)
print(cockatoo)
# print(cockatoo.are_eating())
# print(cockatoo.are_living())
# print(cockatoo.are_moving())
print(cockatoo._areal())
print()
macaque = Monkey('Макака', 3.5)
print(macaque)
# print(macaque.are_eating())
# print(macaque.are_living())
# print(macaque.are_moving())
print(macaque._areal())
print()
lion = Feline('Лев', 5)
print(lion)
# print(lion.are_eating())
# print(lion.are_living())
# print(lion.are_moving())
print(lion._areal())
print()
carp = Fish('Карп', 1.5)
print(carp)
# print(carp.are_eating())
# print(carp.are_living())
# print(carp.are_moving())
print(carp._areal())
