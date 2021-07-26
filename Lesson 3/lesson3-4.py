list = [2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 3, 4, 5, 5, 6, 6, 7, 7, 7, 7]
counter_dict = {}

for n in list:
    if counter_dict.get(n) == None:
        counter_dict[n] = 1
    else:
        aux = counter_dict[n]
        counter_dict[n] = aux + 1

record = [0,0]
for m in counter_dict:
    if counter_dict[m] > record[1]:
        record[0] = m
        record[1] = counter_dict[m]

print("The most ofthen number is " + str(record[0]) + ", and it repeats " + str(record[1]) + " times.")
