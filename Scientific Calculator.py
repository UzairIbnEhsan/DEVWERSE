# Step 1: Import math module
# Why: Provides sin(), cos(), and radians() functions
import math

# Step 2: Define calculator function
# Why: Organizes code into reusable block
def calculator():
    
    # Step 3: Display welcome message
    # Why: Tells user what the program can do
    print("Scientific Calculator By Uzair Ehsan")
    print("Supported operations: +, -, *, /, sin, cos")

    # Step 4: Start infinite loop
    # Why: Keeps calculator running until user types 'end'
    while True:
        
        # Step 5: Try-except for error handling
        # Why: Prevents crashes from invalid input like letters
        try:
            
            # Step 6: Get first number
            # Why: User enters number they want to work with
            a = float(input("\nEnter first number: "))
            
            # Step 7: Get operation choice
            # Why: Ask what to do with the number
            operation = input("Choose an operation (+, -, *, /, sin, cos) or type 'end' to exit: ")
            
            # Step 8: Check if user wants to exit
            # Why: 'break' exits the loop and ends program
            if operation == 'end':
                print("Calculator Power Off")
                break
            
            # Step 9: Validate operation
            # Why: Only allow valid operations from the list
            valid_operations = ['+', '-', '*', '/', 'sin', 'cos']
            if operation not in valid_operations:
                print("Invalid operation! Please choose from: +, -, *, /, sin, cos")
                continue  # Skip to next loop iteration
            
            # Step 10: Handle binary operations (+, -, *, /)
            # Why: These need TWO numbers to calculate
            if operation in ['+', '-', '*', '/']:
                
                # Step 11: Get second number
                # Why: Needed for binary operations
                b = float(input("Enter second number: "))
                
                # Step 12: Perform addition
                # Why: Adds two numbers and shows equation
                if operation == '+':
                    result = a + b
                    print(f"Result: {a} + {b} = {result}")
                
                # Step 13: Perform subtraction
                # Why: Subtracts second number from first
                elif operation == '-':
                    result = a - b
                    print(f"Result: {a} - {b} = {result}")
                
                # Step 14: Perform multiplication
                # Why: Multiplies two numbers together
                elif operation == '*':
                    result = a * b
                    print(f"Result: {a} * {b} = {result}")
                
                # Step 15: Perform division with zero check
                # Why: Division by zero is undefined - must prevent it
                elif operation == '/':
                    if b == 0:
                        print("Error: Division by zero is not allowed!")
                        continue  # Skip without showing result
                    result = a / b
                    print(f"Result: {a} / {b} = {result}")
            
            # Step 16: Handle trig functions (sin, cos)
            # Why: These need ONE number (angle) from first input
            elif operation in ['sin', 'cos']:
                
                # Step 17: Ask for angle type
                # Why: math.sin() needs radians, but users might use degrees
                angle_type = input("Is this in (d)egrees or (r)adians? ")
                
                # Step 18: Convert degrees to radians if needed
                # Why: math.radians() converts degrees to radians for math functions
                if angle_type in ['d', 'degrees']:
                    angle = math.radians(a)
                    unit = "degrees"
                else:
                    angle = a
                    unit = "radians"
                
                # Step 19: Calculate sine
                # Why: math.sin() calculates sine of angle in radians
                if operation == 'sin':
                    result = math.sin(angle)
                    print(f"Result: sin({a} {unit}) = {result}")
                
                # Step 20: Calculate cosine
                # Why: math.cos() calculates cosine of angle in radians
                elif operation == 'cos':
                    result = math.cos(angle)
                    print(f"Result: cos({a} {unit}) = {result}")
                
        # Step 21: Catch ValueError
        # Why: Handles when user types letters instead of numbers
        except ValueError:
            print("Error: Please enter valid numbers!")
        
        # Step 22: Catch any other error
        # Why: Prevents crashes from unexpected errors
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Step 23: Run the calculator
# Why: Ensures calculator runs only when file is executed directly
if __name__ == "__main__":     
    calculator()