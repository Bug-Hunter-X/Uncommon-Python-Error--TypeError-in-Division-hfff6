def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Unsupported operand type(s) for /: 'str' and 'int'"

#Example usage with different inputs
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Division by zero
print(function_with_uncommon_error(10, "hello")) # Output: Unsupported operand type(s) for /: 'int' and 'str'