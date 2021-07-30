from math import sqrt
import cProfile
import timeit

def eratosthenes():
    starttime = timeit.default_timer()
    primes = [2, 3]
    last_crossed = [2, 3]

    def add_next_prime():
        candidate = primes[-1] + 2
        i = 0
        while i < len(primes):
            while last_crossed[i] < candidate:
                last_crossed[i] += primes[i]
            if last_crossed[i] == candidate:
                candidate += 2
                i = 0
            i += 1

        primes.append(candidate)
        last_crossed.append(candidate)

    def fill_primes(n):
        while len(primes) < n:
            add_next_prime()

    fill_primes(168)
    print(primes)
    print("\nFunction eratosthenes takes: " + str(timeit.default_timer() - starttime) + " second.\n")


def found_in_internet(n):
    starttime = timeit.default_timer()
    out = list()
    for num in range(1, n + 1):
        if all(num % i != 0 for i in range(2, num)):
            out.append(num)

    print(out)
    print("\nFunction found_in_internet takes: " + str(timeit.default_timer() - starttime) + " second.\n")
    return out


cProfile.run('eratosthenes()')
cProfile.run('found_in_internet(1000)')

#Erastosthenes algorithm works about 2.5 times faster then 'algorithm found_in_internet'
