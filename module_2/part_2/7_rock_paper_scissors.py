t, r = input(), input()
l = ['камень', 'ножницы', 'бумага']  # вправо - победа; влево - поражение.
if t == r:
    print('ничья')
elif (l.index(t) + 1) % 3 == l.index(r):
    print('Тимур')
else:
    print('Руслан')