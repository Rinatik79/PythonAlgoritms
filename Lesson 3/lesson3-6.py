list = [-2, 3, -4400, 5, 6, 7, -8, 9, 0, 2, 3, 4, 5, 5, 6, 6, -777, 7, 7, 7]
sorted_list = list.copy()
sorted_list.sort()

starting_index = list.index(sorted_list[0]) + 1
ending_index = list.index(sorted_list[len(sorted_list) - 1])

sum = 0

for i in range(starting_index, ending_index):
    sum += list[i]

print(sum)