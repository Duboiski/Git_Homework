# В задаче про класс Human дописать 2 класса:
# класс House для создания дома, класс Buy_House для его покупки.
# Для того, чтобы в классе Human свойство __house сделать True,
# нужно использовать наследование классов. Но каких? :)

class Human:
# Определите для него два статических поля: default_name и default_age.
    default_name = 'USER'
    default_age = None
# Создайте метод __init__(), который помимо self принимает еще два параметра: name и age.
# Для этих параметров задайте значения по умолчанию, используя свойства default_name и default_age.
# В методе __init__() определите четыре свойства: Публичные - name и age. Приватные - money и house.
    def __init__(self, name = default_name, age = default_age):
        #Динамические поля
        #Публичные
        self.name = name
        self.age = age
        #Приватные
        self.__house = False
        self.__money = 0
# Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
    def info(self):
        print(f'Имя: {self.name}, возраст: {self.age}, наличие дома: {self.__house}, денег: {self.__money}')
# Реализуйте справочный статический метод default_info(), который будет выводить
# статические поля default_name и default_age.
    @staticmethod
    def default_info():
        print(f'Имя по умолчанию: {Human.default_name}, возраст по умолчанию: {Human.default_age}')

# Реализуйте метод earn_money(), увеличивающий значение свойства money.
    def earn_money(self, amount):
        self.__money += amount
        print(f'Получили {amount} рублей. Текущий счет: {self.__money} рублей')

# Тесты
# Вызовите справочный метод default_info() для класса Human()
Human.default_info()
# Создайте объект класса Human
Evgeniy = Human('Евгений',29)
# Выведите справочную информацию о созданном объекте (вызовите метод info()).
Evgeniy.info()
# Поправьте финансовое положение объекта - вызовите метод earn_money()
Evgeniy.earn_money(100)
# Посмотрите, как изменилось состояние объекта класса Human
Evgeniy.info()
# print(Evgeniy._Human__money) #обращение к защищенному свойству вне класса (Object._Class__private_method)

class House():
    default_length = 10
    default_width = 9
    default_floors = 1
    default_garage = True
    def __init__(self, length = default_length,
                 width = default_width,
                 floors=default_floors,
                 garage=default_garage):

        self.length = length
        self.width = width
        self.floors = floors
        self.garage = garage
        n = 0
        if self.garage == True:
            n = 10000
        self.price = (((self.length*100)+(self.width*100))*self.floors)+n

    def info(self):
        self.grg = 'нет'
        if self.garage == True:
            self.grg = 'есть'
        print(f'\nВы выбрали дом: длиной = {self.length}м. \n'
              f'шириной = {self.width}м. \n'
              f'этажей - {self.floors} \n'
              f'наличие гаража - {self.grg} \n'
              f'стоимость таково дома будет - {self.price}')

class Buy_House(Human):
    def __init__(self):
        self.length = float(input('Введите желаемую длину дома в метрах: '))
        self.width = float(input('Введите желаемую ширину дома в метрах: '))
        self.floors = int(input('Введите количествоэтажей в доме: '))
        self.grg = int(input('Есть ли гараж (1-да, 2-нет): '))
        if self.grg == 1:
            self.garage = True
        else:
            self.garage = False

        while True:
            my_house = House(self.length, self.width, self.floors, self.garage)
            my_house.info()
            self.shopping = input('Желаете купить? (1-да, 2-нет)')
            if self.shopping == '1':
                if my_house.price <= Evgeniy._Human__money:
                    Evgeniy._Human__money = True
                    print('Поздравляю, вы купили этот дом!')
                    break
                else:
                    print('Не достаточно средств на счете!')
                    print(f'На счете {Evgeniy._Human__money} руб.')
                    self.mon = float(input('Пополнить счет на сумму: '))
                    Evgeniy.earn_money(self.mon)
            else:
                break

new_house = Buy_House()




