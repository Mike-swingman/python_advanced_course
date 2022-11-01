numbers = input().split()
print(*numbers[-1:], *numbers[0:len(numbers)-1])
