class Calculator:
    def calculate(self, a, b, operation):
        if operation == 'addition':
            return a+b
        elif operation == 'subtraction':
            return a-b
        elif operation == 'multiplication':
            return a*b
        elif operation == 'division':
            return a/b if b != 0 else "Error: Division by zero."
        else:
            return "Invalid operation."

a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
operation = input("Enter the operation (addition, subtraction, multiplication, division): ").lower()

calc = Calculator()
result = calc.calculate(a, b, operation)
print(f"Result: {result}")
