from functions import plus, minus, multiply, divide

first = float(input("Number 1: "))
second = float(input("Number 2: "))
operation = input("Operation(+, -, *, /): ")

if operation == "+":
    print(plus(first, second))

elif operation == "-":
    print(minus(first, second))

elif operation == "*":
    print(multiply(first, second))

elif operation == "/":
    print(divide(first, second))
