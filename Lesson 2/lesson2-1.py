def math():
    operation = input("Enter arithmetic operation you want to done for 2 numbers('+', '-', '*', '/') or '0' for exit: ")
    accepted_operations = "+-*/"

    if operation != "0":
        if accepted_operations.find(operation) == -1 or len(operation) != 1:
            print("Incorrect enter, please retry again.")
            math()
        a = float(input("Enter first number please: "))
        b = float(input("Enter second number please: "))

        if b == 0 and operation == "/":
            print("Number cannot be divided by 0, retry please.")
            math()

        elif operation == "/":
            print(a / b)
            math()
        elif operation == "*":
            print(a * b)
            math()
        elif operation == "+":
            print(a + b)
            math()
        else:
            print(a - b)
            math()
    else:
        print("Buy! I'll miss you!")
        exit(0)

math()
