def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error! Modulus by zero is not allowed."
    return a % b

def power(a, b):
    return a ** b

def floor_division(a, b):
    if b == 0:
        return "Error! Floor division by zero is not allowed."
    return a // b


while True:
    print("\n====== PYTHON CALCULATOR ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Floor Division")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    if choice == '8':
        print("Thank you for using the calculator!")
        break

    if choice not in ['1','2','3','4','5','6','7']:
        print("Invalid choice! Please select a valid option.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if choice == '1':
        print("Result =", add(num1, num2))

    elif choice == '2':
        print("Result =", subtract(num1, num2))

    elif choice == '3':
        print("Result =", multiply(num1, num2))

    elif choice == '4':
        print("Result =", divide(num1, num2))

    elif choice == '5':
        print("Result =", modulus(num1, num2))

    elif choice == '6':
        print("Result =", power(num1, num2))

    elif choice == '7':
        print("Result =", floor_division(num1, num2))