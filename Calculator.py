def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def divide(a, b):
    """Divide a by b and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Raise a to the power of b."""
    return a ** b


def main():
    """Main function to demonstrate the calculator."""
    print("Simple Calculator")
    print("-" * 30)
    
    # Example operations
    x, y = 10, 5
    
    print(f"Numbers: {x} and {y}")
    print(f"Addition: {x} + {y} = {add(x, y)}")
    print(f"Subtraction: {x} - {y} = {subtract(x, y)}")
    print(f"Multiplication: {x} * {y} = {multiply(x, y)}")
    print(f"Division: {x} / {y} = {divide(x, y)}")
    print(f"Power: {x} ^ {y} = {power(x, y)}")


if __name__ == "__main__":
    main()
