def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("Select operation: +  -  *  /")
choice = input("Enter choice: ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == "+":
    print(add(a, b))
elif choice == "-":
    print(subtract(a, b))
elif choice == "*":
    print(multiply(a, b))
elif choice == "/":
    print(divide(a, b))
else:
    print("Invalid input")
