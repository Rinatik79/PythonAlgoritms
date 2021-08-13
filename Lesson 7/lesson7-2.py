import random

random_array = []
for i in range(19):
    random_array.append(random.randint(0, 49) + random.random())

print("Array before sorting:")
print(random_array)

list_of_lists = []
for one_float in random_array:
    current_list = []
    current_list.append(one_float)
    list_of_lists.append(current_list)


def merge_sort(given_list, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(given_list, start, mid)
        merge_sort(given_list, mid, end)
        merge_list(given_list, start, mid, end)


def merge_list(given_list, start, mid, end):
    left = given_list[start:mid]
    right = given_list[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            given_list[k] = left[i]
            i = i + 1
        else:
            given_list[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            given_list[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            given_list[k] = right[j]
            j = j + 1
            k = k + 1


merge_sort(list_of_lists, 0, 19)
for i in range(len(random_array)):
    random_array[i] = list_of_lists[i][0]

print('\nArray after sorting:')
print(random_array)
