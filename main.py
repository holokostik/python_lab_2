import csv
import os
import time


def colors(color):  # выводим цвета по их коду
    return f"\u001b[{int(color)}m"


def squares(reps):  # выводим узор
    print(('    ' + white + '  ' + end + '      ' + white + '  ' + end + '     ') * reps)
    print(('  ' + white + '      ' + end + '  ' + white + '      ' + end + '   ') * reps)
    print((white + '                  ' + end + ' ') * reps)
    print(('  ' + white + '      ' + end + '  ' + white + '      ' + end + '   ') * reps)
    print(('    ' + white + '  ' + end + '      ' + white + '  ' + end + '     ') * reps)


def func():  # выводим график заданной функции
    grafic = ['', '', '', '', '', '', '', '', '']
    for rows in range(8, -1, -1):
        grafic[rows] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        for column in range(len(grafic[rows]) - 1):
            if row == column + 1:
                grafic[rows][column] = '*'
        print(grafic[rows])


end = colors('0')  # коды цветов (в т.ч. "пустой" цвет)
red = colors('41')
green = colors('42')
yellow = colors('43')
white = colors('47')

print(green + '  ' + yellow + '    ' + end + '')  # выводим флаг
print(green + '  ' + red + '    ' + end + '')

num_reps = int(input('Сколько раз повторить узор?\n'))
squares(num_reps)

func()

less_price_count = 0  # считаем соотношение книг по ценам
more_price_count = 0
with open("books.csv", "r", encoding='windows-1251') as file:
    reader = csv.reader(file, delimiter=";")
    counter = 0
    for row in reader:
        if counter > 0:
            price = int(float(row[7]))
            if price <= 150:
                less_price_count += 1
            else:
                more_price_count += 1
        counter += 1
print(less_price_count / more_price_count)
print('Дороже 150 рублей:  ' + white + '          ' + end + '  ', more_price_count)
print('\nДешевле 150 рублей: ' + white + '          ' * int(less_price_count / more_price_count) + end + '  ',
      less_price_count)

os.system('cls')  # какая то дурацкая анимация
print('.')
time.sleep(0.5)
os.system('cls')
print('..')
time.sleep(0.5)
os.system('cls')
time.sleep(0.5)
print('...')
