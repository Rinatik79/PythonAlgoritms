divisors = [2, 3, 4, 5, 6, 7, 8, 9]

for divisor in divisors:
    counter = 0

    for i in range(2, 100):
        if i % divisor == 0:
            counter += 1
    print("In range 2-99 there are " + str(counter) + " members which can be divided by " + str(divisor))


# Decided to create second version of this code for homework 6.

print("\nIt will be the same code, but with using tuple:\n")

divisors = (2, 3, 4, 5, 6, 7, 8, 9)

for divisor in divisors:
    counter = 0

    for i in range(2, 100):
        if i % divisor == 0:
            counter += 1
    print("In range 2-99 there are " + str(counter) + " members which can be divided by " + str(divisor))
