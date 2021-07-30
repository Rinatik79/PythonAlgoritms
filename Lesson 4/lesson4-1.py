import cProfile
import timeit

def main():
    starttime = timeit.default_timer()
    divisors = [2, 3, 4, 5, 6, 7, 8, 9]

    for divisor in divisors:
        counter = 0

        for i in range(2, 100):
            if i % divisor == 0:
                counter += 1
        print("In range 2-99 there are " + str(counter) + " members which can be divided by " + str(divisor))

    print("\nFunction main takes: " + str(timeit.default_timer() - starttime) + " second.\n")

cProfile.run('main()')

def main_changed():
    starttime = timeit.default_timer()
    divisors = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

    for divisor in divisors:

        for i in range(2, 100):
            if i % divisor == 0:
                counter = divisors.get(divisor)
                counter += 1
                divisors[divisor] = counter
        print("In range 2-99 there are " + str(divisors[divisor]) + " members which can be divided by " + str(divisor))

    print("\nFunction main_changed takes: " + str(timeit.default_timer() - starttime) + " second.\n")

cProfile.run('main_changed()')
