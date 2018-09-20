res = 0

for index in range(3, 10):
    if((index % 3) == 0) or ((index % 5) == 0):
        res += index

print(res)
