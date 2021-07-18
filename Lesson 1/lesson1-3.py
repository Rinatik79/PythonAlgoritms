a = input("Enter coordinates of first point, x and y should be divided by ';' for example: -0.15;7 :")
b = input("Enter coordinates of second point, x and y should be divided by ';' for example: 2.15;-7 :")

a = a.split(";")
b = b.split(";")
x1 = float(a[0])
x2 = float(b[0])
y1 = float(a[1])
y2 = float(b[1])

k = (y1 - y2) / (x1 - x2)

b = (x1 * y2 - x2 * y1) / (x1 - x2)
if b > 0:
    b = "+" + str(b)
else:
    b = str(b)
print("y = " + str(k) +"x" + b)