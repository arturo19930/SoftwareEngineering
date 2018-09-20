num1 = 1
num2 = 2
res = 0
plus = 2

while res <= 10:
    res = num1 + num2
    num1 = num2 
    num2 = res
    if res % 2 == 0:
        plus += res

print(plus)
