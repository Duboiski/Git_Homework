# 1. Написать рекурсивную функцию, которая определяет, является ли строка палиндромом
# (одинаково читается в обе стороны: герег, лол, мам, level и тд.)
print('Задание 1')
s = input('Введите строку: ')
def is_palindrome(stroka):
    if len(stroka) < 2:
        return True
    elif stroka[0] != stroka[-1]:
        return False
    else:
        if is_palindrome(stroka[1 : -1]) == True:
            return True
        else:
            return False

if is_palindrome(s) == True:
    print('Строка является палиндромом.')
else:
    print('Строка не является палиндромом.')

#2. Написать рекурсивную функцию для подсчета количества элементов в списке.
print('Задание 2')
sp = ('q', 'w', 'd', '4', '5', '6', 'g', 'h', 'j', '10', '11')
print('Список:')
print(sp)
def len_sp(sp):
    if len(sp) > 0:
        return 1 + len_sp(sp[1:])
    else:
        return 0

print(f'Количество элементов в списке = {len_sp(sp)}')

#3. Этот код отсортирует список строк по последнему символу в каждой строке.
    # Здесь использована лямбда-функция в качестве ключа в сортировке.
    # Измените код так, чтобы сортировка была по второму символу каждой строки
print('Задание 3')

strings = ['apple', 'banana', 'cherry', 'date']
print('Список строк:')
print(strings)
sorted_strings = sorted(strings, key=lambda s: s[1])
print('Сортировка по второму символу каждой строки:')
print(sorted_strings) # Output: ['cherry', 'date', 'apple', 'banana']

#4. Напишите функцию make_adder(n),
# которая принимает целое число n и возвращает внутреннюю функцию,
# которая может прибавлять этот n к любому другому целому числу.
print('Задание 4')
def make_adder(n):
    def my_fun(s):
        return n + s
    return my_fun

a = int(input('Введите целое число 1:'))
b = int(input('Введите целое число 2:'))

print(f'Cумма чисел {1} и {2} = {make_adder(a)(b)}')

#5. Напишите функцию counter(), которая возвращает внутреннюю функцию increment(),
# которая увеличивает счетчик на 1 каждый раз, когда она вызывается.
print('Задание 5')
n = int(input('Введите сколько раз вызвать функцию "counter()": '))
s = 0
def counter():
    def increment():
        global s
        s += 1
        return s
    return increment()

print('Количество вызовов функции "counter()":')
for i in range(n):
    print(f'Функия "counter()" вызванна {counter()}-й раз')