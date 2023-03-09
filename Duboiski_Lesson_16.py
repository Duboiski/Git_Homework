# №1. Если в функцию передаётся кортеж, то посчитать длину всех его строк.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.
# Использовать готовые типы данных, с клавиатуры ничего не вводится
# Например function([1,2,3,'a','bc8?']) -> 4 числа, 3 буквы
# function((1,2,3,'a','bc8?',7,8,9)) -> 5 символов
# function(788) -> 1
# function('788') -> 0 букв
# №2. Привяжите к предыдущей функции декоратор, который будет выводить информацию о том,
# какой тип данных вы отправили: кортеж, список, число, строку или какой-то другой тип данных
kr = (1, 2, 3, 'a', 'bc8?', 7, 8, 9)
sp = [1, 2, 3, 'a', 'bc8?']
ch = 788
st = '788'

def my_decorator(fn):
    def wrapper(n):
        if (isinstance(dt, tuple)):
            print(f'В функцию  "my_data" отправлен кортеж')
        elif (isinstance(dt, list)):
            print(f'В функцию  "my_data" отправлен список')
        elif (isinstance(dt, int)):
            print(f'В функцию  "my_data" отправлен число')
        elif (isinstance(dt, str)):
            print(f'В функцию  "my_data" отправлен строка')
        else:
            print('Неопредилённый формат данных')

        print(n)
        fn(n)
    return wrapper

@my_decorator
def my_data(data):
    if (isinstance(dt, tuple)):
        n  = 0
        for i in dt:
            if (isinstance(i, str)):
                n += len(i)
        return print(f'В кортеже {dt} длина всех строк ровна {n} символов')

    elif (isinstance(dt, list)):
        n_number = 0
        n_letter = 0
        for i in dt:
            # lst = dt[i]
            for j in str(i):
                if j.isdigit():
                    n_number += 1
                if j.isalpha():
                    n_letter += 1
        return print(f'В списке - {dt} ==> {n_number} числа и {n_letter} буквы')

    elif (isinstance(dt, int)):
        n = 0
        for i in str(dt):
            if int(i)%2 != 0:
                n += 1
        return print(f'В числе - {dt} количество нечётных цифр = {n}')

    elif (isinstance(dt, str)):
        n_letter = 0
        for i in dt:
            if i.isalpha():
                n_letter += 1
        return print(f'В строке - {dt} количество букв = {n_letter}')

print('Пустой ввод - выход из программы')
while True:
    s = input('Что передать в функцию? \n'
              '1 - кортеж, 2 - список, 3 - число, 4 - строка \n'
              'или введите свои данные: ')
    if s == '':
        break

    if s.isdigit():
        if int(s) == 1:
            dt = kr
        elif int(s) == 2:
            dt = sp
        elif int(s) == 3:
            dt = ch
        elif int(s) == 4:
            dt = st
        else:
            dt = int(s)

    elif s[0] == '(' and s[-1] == ')':
        s = s[1: -1]
        s2 = ''

        for i in range(len(s)):
            if not (s[i] == '"' or s[i] == "'"):
                s2 += s[i]

        s2 = s2.split(',')

        for i in range(len(s2)):
            if s2[i].isdigit():
                s2[i] = int(s2[i])

        dt = tuple(s2)
    elif s[0] == '[' and s[-1] == ']':
        s = s[1: -1]
        s2 = ''

        for i in range(len(s)):
            if not (s[i] == '"' or s[i] == "'"):
                s2 += s[i]
        s2 = s2.split(',')

        for i in range(len(s2)):
            if s2[i].isdigit():
                s2[i] = int(s2[i])

        dt = list(s2)
    else:
        dt = str(s)

    my_data(dt)
