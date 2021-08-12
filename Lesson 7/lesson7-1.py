import random

random_array = []
for i in range(19):
    random_array.append(random.randint(0, 100))

print("Array before sorting:")
print(random_array)


for i in range(18, 0, -1):
    #min = random_array[i]
    print(i)
    for j in range(i - 1, -1, -1):
        if random_array[j] < random_array[i]:
            min = random_array[j]
            random_array[j] = random_array[i]
            random_array[i] = min

print("\nArray after sorting:")
print(random_array)
