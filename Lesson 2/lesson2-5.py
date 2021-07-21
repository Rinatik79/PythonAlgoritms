current = 32
line = ""
counter = 0
while current <= 127:
    line += str(current) + " " + chr(current) + "\t"
    current += 1
    if counter != 9:
        counter += 1

    else:
        counter = 0
        print(line)
        line = ""

print(line)
