# Калькулятор. Создать класс, где реализованы методы математических операция (+-/*)
# и функция (вне класса) для ввода данных.
class Calculator:
    def performance(self):
        print('\nПустой ввод выход...')
        self.a = input('Введите первое число: ')
        if self.a == '':
            return False
        else:
            self.a = float(self.a)

        self.zn = input('Введите знак операции ( +, -, *, / ): ')
        if self.zn == '':
            return False

        self.b = input('Введите второе число: ')
        if self.b == '':
            return False
        else:
            self.b = float(self.b)

        if self.zn == '+':
            print(self.a + self.b)
        elif self.zn == '-':
            print(self.a - self.b)
        elif self.zn == '*':
            print(self.a * self.b)
        elif self.zn == '/':
            print(self.a / self.b)
        else:
            print('Такая операция не потдерживается.')

calc = Calculator()

while True:
    if calc.performance() == False:
        break
