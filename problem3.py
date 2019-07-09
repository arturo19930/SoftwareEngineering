number = 600851475143
prime = 2
largest_prime = 0

while number != 1:
    if (number % prime) == 0:
        number /= prime
        largest_prime = prime
    else:
        prime += 1

print(prime)
