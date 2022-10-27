w = float(input())
g = float(input())
if w / g ** 2 < 18.5:
    print('Недостаточная масса')
elif w / g ** 2 > 25:
    print('Избыточная масса')
else:
    print('Оптимальная масса')
