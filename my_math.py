def math_operations(a, b):
    """
    Perform basic math operations on two numbers.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    dict: A dictionary containing the results of addition, subtraction,
          multiplication, and division.
    """
    return {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'division': a / b if b != 0 else 'undefined'
    }

def add(*args):
    """Add two or more numbers."""
    sum = 0
    for arg in args:
        sum += arg
    return sum


if __name__ == "__main__":
    # Example usage
    result = add(1, 2, 3, 4)
    print(result)