number_1 = 3
number_2 = 5
sum = 0

for x in range(1000):
    if x % number_1 == 0 or x % number_2 == 0:
        sum += x

print(sum)