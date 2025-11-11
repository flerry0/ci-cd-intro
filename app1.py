def add(a, b):
    """Addiert zwei Zahlen"""
    return a + b


def subtract(a, b):
    """Subtrahiert zwei Zahlen"""
    return a - b


def multiply(a, b):
    """Multipliziert zwei Zahlen"""
    return a * b


def divide(a, b):
    """Dividiert zwei Zahlen"""
    if b == 0:
        raise ValueError("Division durch Null ist nicht erlaubt")
    return a / b


if __name__ == "__main__":
    print("Rechner-App")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")
    print(f"6 / 3 = {divide(6, 3)}")
