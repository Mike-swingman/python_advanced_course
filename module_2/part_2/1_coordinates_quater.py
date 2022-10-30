num = int(input())
quarter_1 = 0
quarter_2 = 0
quarter_3 = 0
quarter_4 = 0
for i in range(num):
    coordinates = list(map (int, input().split()))
    if coordinates[0] > 0 and coordinates[1] > 0:
        quarter_1 += 1
    if coordinates[0] < 0 and coordinates[1] > 0:
        quarter_2 += 1
    if coordinates[0] < 0 and coordinates[1] < 0:
        quarter_3 += 1
    if coordinates[0] > 0 and coordinates[1] < 0:
        quarter_4 += 1
    coordinates.clear()
print(f'Первая четверть: {quarter_1}')
print(f'Вторая четверть: {quarter_2}')
print(f'Третья четверть: {quarter_3}')
print(f'Четвертая четверть: {quarter_4}')
