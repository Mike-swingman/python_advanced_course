num = input()
if len(num) == 5:
    print(int(num[::-1]))
else:
    print(num[0] + num[5:0:-1])