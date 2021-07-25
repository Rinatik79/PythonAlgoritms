divisors = [2, 3, 4, 5, 6, 7, 8, 9]

for divisor in divisors:
    counter = 0

    for i in range(2, 100):
        if i % divisor == 0:
            counter += 1
    print("In range 2-99 there are " + str(counter) + " members which can be divided by " + str(divisor))