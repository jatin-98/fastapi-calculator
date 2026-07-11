import pytest
from app.services.calculator import perform_calculation


def test_perform_calculation_add():
    assert perform_calculation(5.0, 3.0, "add") == 8.0


def test_perform_calculation_subtract():
    assert perform_calculation(5.0, 3.0, "subtract") == 2.0


def test_perform_calculation_multiply():
    assert perform_calculation(5.0, 3.0, "multiply") == 15.0


def test_perform_calculation_divide():
    assert perform_calculation(6.0, 3.0, "divide") == 2.0


def test_perform_calculation_invalid_operation():
    with pytest.raises(ValueError, match="Invalid Operation"):
        perform_calculation(5.0, 3.0, "invalid")
