def function_with_uncommon_error_solution(a, b):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        print("Error: Invalid input types. Inputs must be numbers.")
        return None
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None

# Example usage
result1 = function_with_uncommon_error_solution(10, 2)  # Valid input
print(result1)  # Output: 5.0

result2 = function_with_uncommon_error_solution(10, 0)  # ZeroDivisionError
print(result2)  # Output: Error: Division by zero
None

result3 = function_with_uncommon_error_solution(10, 'a')  #Invalid Input
print(result3) # Output: Error: Invalid input types. Inputs must be numbers.
None