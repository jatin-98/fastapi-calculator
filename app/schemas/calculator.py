from pydantic import BaseModel, Field


class CalculatorRequest(BaseModel):
    expression: str = Field(..., min_length=1, description="Expression to evaluate")


class CalculatorResponse(BaseModel):
    result: float = Field(..., description="Result of the evaluation")
