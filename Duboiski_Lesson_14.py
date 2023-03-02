# 1. Напишите функцию, которая принимает на вход два аргумента и возвращает их сумму.
print('Задание 1')
s = 2
x = 5
def my_sum(a, b):
    return a + b

print(f"Аргумент 1: {s}, аргумент 2: {x}, их сумма: {my_sum(s, x)} ")

# 2. Напишите функцию, которая принимает на вход список чисел и возвращает их среднее значение.
import random
print('Задание 2')
s = [random.randint(1, 10) for i in range(10)]
def my_value(x):
    n = 0
    for i in x:
        n = n + i
    return n / len(x)

print(f'Список: {s}')
print(f'Среднее значение: {my_value(s)}')

# 3. Напишите функцию, которая принимает на вход число и возвращает True,
# если оно четное, и False, если оно нечетное.
import random
print('Задание 3')
s = random.randint(1, 10)
def chet_not_chet(x):
    if x%2 == 0:
        return True
    else:
        return False

print(f'Число {s} чётное?')
print(f'Ответ: {chet_not_chet(s)}')

# 4. Напишите функцию, которая принимает на вход список и
# возвращает новый список, содержащий только уникальные
# элементы из исходного списка.
import random
print('Задание 4')
s = [random.randint(1, 10) for i in range(10)]
print(f'Список: {s}')
def unique_list(x):
    a = []
    for i in x:
        if i not in a:
            a.append(i)
    return a

print(f'Уникальные элементы: {unique_list(s)}')

# 5. Решите задачу с использованием вложенной функции is_square.
# Предположим, у нас есть список чисел и мы хотим найти все числа,
# которые являются квадратами других чисел в этом списке.
print('Задание 5')
s = [2, 1, 4, 5, 3, 9, 0, 10, 16]
def find_square_numbers(numbers):
    def is_square(number):
        return number ** 2
    f = []
    for i in numbers:
        if (i == 1) or (i == 0):
            continue
        if is_square(i) in numbers:
            f.append(is_square(i))

    return f

print(f'Список: {s}')
print(f'Имеются квадраты: {find_square_numbers(s)}')