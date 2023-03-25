# 1.	Создайте класс "Студент", который имеет атрибуты имя и возраст,
# а также методы "изменить_имя" и "изменить_возраст". Напишите функцию,
# которая создает объект класса "Студент", запрашивая у пользователя его
# имя и возраст, а затем предлагает пользователю изменить имя и возраст.
# import self as self

print('Задание 1')
class Student:
    name = ''
    age = 0
    def change_name(self, name):
        self.name = name
    def change_age(self, age):
        self.age = age

def new_student():
    std = Student()
    name = input('Введите своё имя:')
    age = input('Введите свой возраст:')
    std.name = name
    std.age = age
    print(f'Вы зарегистрировались как {std.name} и ваш возраст {std.age} лет')
    rename = int(input('Хотите изменить свои данные? (1-да, 2-нет): '))

    if rename == 1:
        name = input('Введите своё имя:')
        age = input('Введите свой возраст:')
        std.change_name(name)
        std.change_age(age)
        print(f'Вы перерегистрировались как {std.name} и ваш возраст {std.age} лет')

new_student()

# 2. Напишите функцию, которая принимает на вход список чисел и
#    возвращает сумму квадратов всех четных чисел в списке.

print('Задание 2')
import random
s = [random.randint(1,10) for i in range(10)]
print('Список:')
print(s)
def my_sum(spisok):
    n = 0
    for i in spisok:
        if i % 2 == 0:
            n += i ** 2
    return n

print(f'Сумму квадратов всех четных чисел в списке = {my_sum(s)}')

# 3.Создайте класс "Калькулятор", который имеет атрибуты "значение" и
#   методы "сложить", "вычесть", "умножить" и "разделить". Напишите функцию,
#   которая создает объект класса "Калькулятор" и позволяет пользователю
#   выполнить несколько арифметических операций с его помощью.
print('Задание 3')
class Calculator:
    a = 0
    b = 0
    def addition(self, a, b):
        return a + b
    def subtraction(self, a, b):
        return a - b
    def multiplication(self, a, b):
        return a * b
    def division(self, a, b):
        return a / b

def calculator():
    calc = Calculator()
    while True:
        print('Пустой ввод выход...')
        a = input('Введите первое число: ')
        if a == '':
            break
        else:
            a = float(a)

        zn = input('Введите знак операции ( +, -, *, / ): ')
        if zn == '':
            break

        b = input('Введите второе число: ')
        if b == '':
            break
        else:
            b = float(b)

        if zn == '+':
            print(calc.addition(a, b))
        elif zn == '-':
            print(calc.subtraction(a, b))
        elif zn == '*':
            print(calc.multiplication(a, b))
        elif zn == '/':
            if b == 0:
                print('Делить на ноль нельзя.')
            else:
                print(calc.division(a, b))
        else:
            print('Такая операция не потдерживается...')

calculator()

# 4.Создайте класс "Автомобиль", который имеет атрибуты "марка", "модель", "год_выпуска",
#     "цвет" и метод "описание", который выводит описание автомобиля в виде строки.
#     Напишите функцию, которая создает объект класса "Автомобиль", запрашивая у пользователя
#     информацию о марке, модели, годе выпуска и цвете, а затем выводит описание автомобиля.
print('Задание 4')
class Car:
    brand = ''
    model = ''
    year = 1900
    color = ''
    def description(self):

        return f'Марка автомобиля: {self.brand} \n' \
               f'Модель автомобиля: {self.model} \n' \
               f'Год выпуска автомобиля: {self.year} \n' \
               f'Цвет автомобиля: {self.color}'

def automobile():
    auto = Car()
    auto.brand = input('Введите марку автомобиля: ')
    auto.model = input('Введите модель автомобиля: ')
    auto.year = input('Введите год выпуска автомобиля: ')
    auto.color = input('Введите цвет автомобиля: ')
    print(auto.description())

automobile()

# 5.Создайте класс "Сотрудник", который имеет атрибуты
#     "имя", "фамилия", "должность" и метод "описание",
#     который выводит описание сотрудника в виде строки.
#     Создайте класс "Отдел", который имеет атрибуты "название"
#     и "список_сотрудников", а также методы "добавить_сотрудника"
#     и "удалить_сотрудника". Напишите функцию, которая создает
#     объект класса "Отдел", запрашивая у пользователя его название,
#     а затем предлагает пользователю добавить несколько сотрудников
#     в отдел, после чего выводит список всех сотрудников в отделе и
#     их описания. Затем функция предлагает пользователю удалить
#     одного из сотрудников и выводит обновленный список сотрудников
#     и их описания.
print('Задание 5')
class Employee:
    def __init__(self, name, surname, job_title):
        self.name = name
        self.surname = surname
        self.job_title = job_title
    def description(self):
        return f'{self.name} {self.surname} - {self.job_title}'
    def __str__(self):
        return f'{self.name} {self.surname} - {self.job_title}'

class Department:
    def __init__(self):
        self.dep_name = 'Отдел_1'
        self.staff = {}

    def add_employee(self, number, employee):
        self.staff[number] = employee

    def remove_employee(self, employee):
        for key, value in self.staff.items():
            if value == employee:
                n = key
        del self.staff[n]

def company():
    my_company = Department()
    my_company.dep_name = input('Введите название отдела: ')
    employee_number = 0
    while True:
        n = int(input('Добавить сотрудника? (1-да, 2-закончить добавление) '))
        if  n == 2:
            break
        elif n == 1:
            employee_name = input('Введите имя: ')
            employee_surname = input('Введите фамилию: ')
            employee_job_title = input('Введите должность: ')
            if employee_name != '' and employee_surname != '' and employee_job_title != '':
                emp = [employee_name, employee_surname, employee_job_title]
                my_company.add_employee(employee_number, emp)
                employee_number += 1
        else:
            print('Введите 1 или 2')

    result = [Employee(*value) for key, value in my_company.staff.items()]
    for info in result:
        print(info)

    while True:
        n = int(input('Удалить сотрудника? (1-да, 2-закончить добавление) '))
        if n == 2:
            break
        elif n == 1:
            employee_name = input('Введите имя: ')
            employee_surname = input('Введите фамилию: ')
            employee_job_title = input('Введите должность: ')
            if employee_name != '' and employee_surname != '' and employee_job_title != '':
                emp = [employee_name, employee_surname, employee_job_title]
                my_company.remove_employee(emp)
        else:
            print('Введите 1 или 2')

        result = [Employee(*value) for key, value in my_company.staff.items()]
        for info in result:
            print(info)


company()