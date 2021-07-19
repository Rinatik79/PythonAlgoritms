numbers = input("Enter 3 numbers separated by ';' : ")

numbers = numbers.split(";")
numbers[0] = float(numbers[0])
numbers[1] = float(numbers[1])
numbers[2] = float(numbers[2])

if (numbers[0]<numbers[1] and numbers[0] > numbers[2]) or (numbers[0] > numbers[1] and numbers[0] < numbers[2]):
    print("Average number is " + str(numbers[0]))

elif (numbers[1]<numbers[2] and numbers[1] > numbers[0]) or (numbers[1] > numbers[2] and numbers[1] < numbers[0]):
    print("Average number is " + str(numbers[1]))

elif (numbers[2]<numbers[0] and numbers[2] > numbers[1]) or (numbers[2] > numbers[0] and numbers[2] < numbers[1]):
    print("Average number is " + str(numbers[2]))

else:
    print("There isn't one single average number")
