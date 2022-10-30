num = input()
num1 = ''
while int(num) > 999:
    num1 = ',' + num[-3:] + num1
    num = num[:-3]
print(str(num) + num1)