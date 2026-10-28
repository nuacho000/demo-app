def greet(name):
    """Return a greeting for the given name."""
    if not isinstance(name, str):
        raise TypeError("name must be a string")

    name = name.strip()
    if not name:
        raise ValueError("name cannot be empty")

    return f"Hello, {name}!"


def add(a, b):
    """Return the sum of two numbers."""
    return a + b
