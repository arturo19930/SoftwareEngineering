num = 600851475143
index = 2
prime = 0

while num != 1:
    if (num & index) == 0:
        num /= index
        prime = index
    else:
        index += 1

print(prime)
