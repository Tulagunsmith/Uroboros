#  Программа, которая определяет знак зодиака
month = input('Введите месяц: ').lower()
day = int(input('Введите число: '))
zodiak = ['Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы']
if month == 'март' and day in range(21, 32) or month == 'апрель' and day in range(1, 21):
    print('Вывод: ', zodiak[0], sep='\n')
if month == 'май' and day in range(1, 22) or month == 'апрель' and day in range(21, 31):
    print('Вывод: ', zodiak[1], sep='\n')
if month == 'май' and day in range(22, 32) or month == 'июнь' and day in range(1, 22):
    print('Вывод: ', zodiak[2], sep='\n')
if month == 'июль' and day in range(1, 23) or month == 'июнь' and day in range(22, 31):
    print('Вывод: ', zodiak[3], sep='\n')
if month == 'июль' and day in range(22, 32) or month == 'август' and day in range(1, 22):
    print('Вывод: ', zodiak[4], sep='\n')
if month == 'сентябрь' and day in range(1, 24) or month == 'август' and day in range(22, 32):
    print('Вывод: ', zodiak[5], sep='\n')
if month == 'сентябрь' and day in range(24, 31) or month == 'октябрь' and day in range(1, 24):
    print('Вывод: ', zodiak[6], sep='\n')
if month == 'ноябрь' and day in range(1, 23) or month == 'октябрь' and day in range(24, 32):
    print('Вывод: ', zodiak[7], sep='\n')
if month == 'ноябрь' and day in range(23, 30) or month == 'декабрь' and day in range(1, 23):
    print('Вывод: ', zodiak[8], sep='\n')
if month == 'январь' and day in range(1, 21) or month == 'декабрь' and day in range(23, 32):
    print('Вывод: ', zodiak[9], sep='\n')
if month == 'январь' and day in range(21, 31) or month == 'февраль' and day in range(1, 20):
    print('Вывод: ', zodiak[10], sep='\n')
if month == 'март' and day in range(1, 21) or month == 'февраль' and day in range(20, 30):
    print('Вывод: ', zodiak[11], sep='\n')
