accepted_operations = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b,
}


def perform_calculation(a: float, b: float, operation: str) -> float:
    try:
        return accepted_operations.get(operation)(a, b)

    except Exception:
        raise ValueError("Invalid operation")
