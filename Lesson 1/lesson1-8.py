import datetime

year = int(input("Enter year number for checking is it leap: "))


try:
    x = datetime.datetime(year, 2, 29)
    print("Year " + str(year) + " is leap.")

except ValueError:
    print("Year " + str(year) + " isn't leap.")
