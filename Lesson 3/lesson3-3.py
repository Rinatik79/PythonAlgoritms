import random

random_list = []
for i in range(100):
    random_list.append(random.randint(-1000, 1000))

min = [random_list[0], 0]
max = [random_list[99], 99]

for i in range(len(random_list)):
    if min[0] > random_list[i]:
        min = [random_list[i], i]
    if max[0] < random_list[i]:
        max = [random_list[i], i]

random_list[min[1]] = max[0]
random_list[max[1]] = min[0]
