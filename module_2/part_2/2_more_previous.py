numbers = list(map (int, input().split()))
counter = 0
for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i + 1]:
        counter += 1
print(counter)
