def calculator():
    """Performs basic calculations and allows for continued operation."""

    global result  # Keep track of the result between function calls

    try:
        # Use existing result if available
        first_number = int(result)
        print(f"Using previous result ({first_number}) as the first number.")
    except NameError:
        # Start fresh if the result is not yet defined
        first_number = int(input("Enter the first number: "))

    operation = input("Enter the operation (+, -, *, /): ")
    second_number = int(input("Enter the second number: "))

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = first_number / second_number
    else:
        print("Invalid operation.")
        return  

    print(f"The result is: {result}")

    continue_choice = input("Do you want to continue? (y/n): ")
    if continue_choice.lower() == "y":
        calculator()  
    # No need to handle 'n' explicitly, as the function will end naturally

# Start the calculator
calculator()
