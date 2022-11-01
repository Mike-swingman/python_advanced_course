word = input() + ' запретил букву'
zz = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
for i in range(32):
    if zz[i] in word:
        print(word.replace('  ', ' ').strip(), zz[i])
        word = word.replace(zz[i], '')