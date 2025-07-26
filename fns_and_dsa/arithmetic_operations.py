def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            operation = num1 + num2
        case "subtract":
            operation = num1 - num2
        case "multiply":
            operation = num1 * num2
        case "divide":
            if num2 == 0:
                message = "Cannot divide by 0"
                return message
            else:
                operation = num1 / num2
    return operation