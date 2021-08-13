import random
import statistics

random_array = []
m = int(input("Enter m you want: "))
for i in range(2 * m +1):
    random_array.append(random.randint(0, 100))

print("This list of random int was generated:")
print(random_array)

print("\nMedian is an item with value:")
print(statistics.median(random_array))