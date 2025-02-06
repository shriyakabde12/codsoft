# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display operation choices
print("Choose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get user choice
choice = input("Enter choice (1/2/3/4): ")

# Perform calculation based on user choice
if choice == '1':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid input! Please choose a valid operation.")