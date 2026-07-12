import pytest
from app.services.calculator import evaluate_expression


def test_evaluate_expression_add():
    assert evaluate_expression("5.0 + 3.0") == 8.0


def test_evaluate_expression_subtract():
    assert evaluate_expression("5.0 - 3.0") == 2.0


def test_evaluate_expression_multiply():
    assert evaluate_expression("5.0 * 3.0") == 15.0


def test_evaluate_expression_divide():
    assert evaluate_expression("6.0 / 3.0") == 2.0


def test_evaluate_expression_chained():
    assert evaluate_expression("1 + 5 + 7 - 2") == 11.0


def test_evaluate_expression_parenthesis():
    assert evaluate_expression("(10 + 5) * 2") == 30.0


def test_evaluate_expression_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        evaluate_expression("1 / 0")


def test_evaluate_expression_unary_minus():
    assert evaluate_expression("-5 + 3") == -2.0


def test_evaluate_expression_invalid_operation():
    with pytest.raises(ValueError):
        evaluate_expression("invalid")


def test_evaluate_expression_security_eval():
    with pytest.raises(ValueError, match="Unsupported syntax"):
        evaluate_expression("eval('1+1')")


def test_evaluate_expression_security_import():
    with pytest.raises(ValueError, match="Unsupported syntax"):
        evaluate_expression("__import__('os').system('echo hello')")
