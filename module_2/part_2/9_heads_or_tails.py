string = input()
counter_max = 0
counter = 0
for i in string:
    if i == 'Р':
        counter += 1
        counter_max = max(counter, counter_max)
    else:
        counter = 0
print(counter_max)