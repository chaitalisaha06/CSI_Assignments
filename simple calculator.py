import math

def evaluate_expression(expression):
    try:
        # Evaluate the expression using eval
        result = eval(expression, {"__builtins__": None}, {"sqrt": math.sqrt})
        return result
    except Exception as e:
        return "INVALID INPUT"

def calculator():
    print("Simple Calculator")
    print("Type 'exit' to end the program")
    print("Supported operations: +, -, *, /, ** (power), sqrt()")
    
    while True:
        # Get the user input
        expression = input("Enter expression: ")
        
        # Exit the program if user types 'exit'
        if expression.lower() == 'exit':
            print("THANK YOU ")
            break
        
        # Evaluate and print the result
        result = evaluate_expression(expression)
        print("Result:", result)

if __name__ == "__main__":
    calculator()
