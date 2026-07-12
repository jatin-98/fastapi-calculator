import ast
import numpy as np

# Map AST operator nodes to NumPy functions
_AST_OPERATORS = {
    ast.Add: np.add,
    ast.Sub: np.subtract,
    ast.Mult: np.multiply,
    ast.Div: np.divide,
    ast.USub: np.negative,  # Handles unary minus (e.g., -5)
    ast.UAdd: np.positive,  # Handles unary plus (e.g., +5)
}


def _eval_node(node) -> float:
    """Recursively evaluate an AST node safely."""
    # If it's the root expression node, evaluate its body
    if isinstance(node, ast.Expression):
        return _eval_node(node.body)

    # If it's a constant number (e.g., 5 or 3.14)
    elif isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return float(node.value)
        raise ValueError(f"Unsupported constant type: {type(node.value).__name__}")

    # If it's a binary operation (e.g., 1 + 2)
    elif isinstance(node, ast.BinOp):
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        op_type = type(node.op)

        if op_type in _AST_OPERATORS:
            return float(_AST_OPERATORS[op_type](left, right))
        raise ValueError(f"Unsupported operator: {op_type.__name__}")

    # If it's a unary operation (e.g., -5)
    elif isinstance(node, ast.UnaryOp):
        operand = _eval_node(node.operand)
        op_type = type(node.op)

        if op_type in _AST_OPERATORS:
            return float(_AST_OPERATORS[op_type](operand))
        raise ValueError(f"Unsupported unary operator: {op_type.__name__}")

    # Block absolutely everything else (functions, variables, assignments, eval, os, etc.)
    raise ValueError(f"Unsupported syntax: {type(node).__name__}")


def evaluate_expression(expression: str) -> float:
    try:
        # Parse the string into an AST in 'eval' mode
        # This safely builds the tree but executes NOTHING
        tree = ast.parse(expression, mode="eval")
    except SyntaxError:
        raise ValueError("Invalid mathematical expression")

    # Walk down the tree and calculate the math
    return _eval_node(tree)
