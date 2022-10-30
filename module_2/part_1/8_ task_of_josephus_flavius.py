n, k = int(input()), int(input())
index = k - 1
people = list(i for i in range(1, n + 1))
while len(people) > 1:
    del people[index]
    index = (index - 1 + k) % len(people)
print(people[0])