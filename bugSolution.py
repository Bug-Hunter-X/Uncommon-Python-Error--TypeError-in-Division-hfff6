def function_with_uncommon_error(a, b):
    try:
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            result = a / b
            return result
        else:
            return "Unsupported operand type(s) for /: only int and float are supported"
    except ZeroDivisionError:
        return "Division by zero"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

#Example usage with different inputs
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Division by zero
print(function_with_uncommon_error(10, "hello")) # Output: Unsupported operand type(s) for /: only int and float are supported
print(function_with_uncommon_error("hello",10)) # Output: Unsupported operand type(s) for /: only int and float are supported