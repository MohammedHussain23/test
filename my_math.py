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

def sub(*args):
    """Subtract two or more numbers."""
    if len(args) < 2:
        raise ValueError("At least two numbers are required for subtraction.")
    sub = args[0]
    for arg in args[1:]:
        sub -= arg
    return sub

if __name__ == "__main__":
    # Example usage
    inp = int(input("1 for add and 2 for sub: "))
    result = sub(3, 1, 2) if inp == 2 else add(3, 1, 2)
    print(result)