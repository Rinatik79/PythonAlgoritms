list = [-2, 3, -4400, 5, 6, 7, -8, 9, 0, 2, 3, 4, 5, 5, 6, 6, -777, 7, 7, 7]
sorted_list = list.copy()
sorted_list.sort()

if sorted_list[0] < 0:
    print("The biggest negative element in list is " + str(sorted_list[0]) + " and his index is " + str(list.index(sorted_list[0])))

else:
    print("Given list doesn't contain any negative number.")
