import numpy as np

accepted_operations = {
    "add": np.add,
    "subtract": np.subtract,
    "multiply": np.multiply,
    "divide": np.divide,
}


def perform_calculation(a: float, b: float, operation: str) -> float:
    action = accepted_operations.get(operation)
    if not action:
        raise ValueError("Invalid Operation")
    return float(action(a, b))
