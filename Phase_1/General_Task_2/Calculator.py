# num1 = float(input("Enter first number: "))
# op = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# if op == '+':
#     result = num1 + num2
# elif op == '-':
#     result = num1 - num2
# elif op == '*':
#     result = num1 * num2
# elif op == '/':
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error: Division by zero"
# else:
#     result = "Error: Invalid operator"

# print("Result:", result)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operator(prompt):
    while True:
        op = input(prompt)
        if op in ['+', '-', '*', '/']:
            return op
        else:
            print("Invalid operator. Please enter one of +, -, *, /.")

def calculate(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
        
def main():
    num1 = get_number("Enter first number: ")
    op = get_operator("Enter operator (+, -, *, /): ")
    num2 = get_number("Enter second number: ")
    
    result = calculate(num1, op, num2)
    print("Result:", result)

if __name__ == "__main__":
    main()