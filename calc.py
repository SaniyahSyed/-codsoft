# Function to perform arithmetic operations
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Invalid operator"

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation
    result = calculate(num1, num2, operator)

    # Display the result
    print(f"Result: {result}")

except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
