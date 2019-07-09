fibonacci = 0
number_1 = 1  # First value of the Fibonacci
number_2 = 2  # Second value of the Fibonacci
result = 2    # We start in "2" as this an even-number.

while fibonacci < 4000000:
    fibonacci = number_1 + number_2
    number_1 = number_2
    number_2 = fibonacci
    if fibonacci % 2 == 0 and fibonacci < 4000000:
        result += fibonacci

print(result)
