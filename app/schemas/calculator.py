from pydantic import Field
from pydantic import BaseModel


class CalculatorRequest(BaseModel):
    expression: str = Field(..., description="Expression to evaluate")


class CalculatorResponse(BaseModel):
    result: float = Field(..., description="Result of the evaluation")
