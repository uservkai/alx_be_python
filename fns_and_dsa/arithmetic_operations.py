def perform_operation(num1, num2, operation):
    
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    else:
        if num2 == 0:
            result = "Cannot divide by 0"
        else:
            result = num1 / num2
    return result