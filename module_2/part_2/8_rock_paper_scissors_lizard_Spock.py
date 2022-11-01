t, r = input(), input()
var = ['ножницы','бумага', 'камень', 'ящерица', 'Спок']
index_t = var.index(t)
index_r = var.index(r)
if (index_t + 1) % 5 == index_r or (index_t + 3) % 5 == index_r:
    print('Тимур')
elif index_t == index_r:
    print('ничья')
else:
    print('Руслан')