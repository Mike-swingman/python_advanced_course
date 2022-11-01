numbers = [int(input()) for i in range(int(input()))]
result = int(input())
flag = False
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] * numbers[j] == result:
            flag = True
            break
if flag == True:
    print('ДА')
else:
    print('НЕТ')