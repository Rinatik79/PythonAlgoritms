sides = input("Enter length of every side of triangle, separated by ';' : ")

sides = sides.split(";")
sides[0] = float(sides[0])
current = sides[0]
sides[1] = float(sides[1])
if sides[1] > sides[0]:
    sides[0] = sides[1]
    sides[1] = current
    current = sides[0]
sides[2] = float(sides[2])
if sides[2] > sides[0]:
    sides[0] = sides[2]
    sides[2] = current;

if sides[0] > sides[1] + sides[2]:
    print("Triangle with given sides doesn't exist.")
elif sides[1] == sides[2]:
    print("This is isosceles triangle.")
if sides[0] == sides[1] == sides[2]:
    print("This is equilateral triangle.")


