import ast
import operator

_AST_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
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
            try:
                return float(_AST_OPERATORS[op_type](left, right))
            except ZeroDivisionError:
                raise ValueError("Division by zero is not allowed")
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
    """
    Safely evaluates a mathematical expression string using an Abstract Syntax Tree (AST).

    Args:
        expression (str): The mathematical expression to evaluate (e.g., "1 + 5 * 2").

    Returns:
        float: The calculated result.

    Raises:
        ValueError: If the expression contains invalid syntax, unsupported operations, or division by zero.
    """
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError:
        raise ValueError("Invalid mathematical expression")

    return _eval_node(tree)
