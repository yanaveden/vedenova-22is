a = input('Введите длину волны: ')

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели!')
        a = input('Введите длину волны: ')

if a <= 450:
    print('Фиолетовый')
elif 450 < a <= 480:
    print('Синий')
elif 480 < a <= 510:
    print('Сине-зеленый')
elif 510 < a <= 550:
    print('Зеленый')
elif 550 < a <= 570:
    print('Желто-зеленый')
elif 570 < a <= 590:
    print('Желтый')
elif 590 < a <= 630:
    print('Оранжевый')
else:
    print('Красный')
