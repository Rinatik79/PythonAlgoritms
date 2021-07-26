matrix = []
print("Let's create matrix 5 x 5 by entering 5 lines with 4 elements separated by ' '.")
print("The fifth element of every line will be sum of all line numbers.")
for i in range(0, 5):
    line = input("Please enter numbers for line number " + str(i) + ": ").split()
    sum = 0
    for j in range(4):
        line[j] = int(line[j])
        sum += line[j]

    line.append(sum)
    matrix.append(line)

print("Here is our matrix:")
print(*matrix, sep = "\n")
