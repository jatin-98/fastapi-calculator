from fastapi.routing import APIRouter
from app.services.calculator import evaluate_expression
from app.schemas.calculator import CalculatorRequest, CalculatorResponse
from fastapi import HTTPException

router = APIRouter()


@router.post("/", response_model=CalculatorResponse)
def calculate(request: CalculatorRequest):
    try:
        result = evaluate_expression(request.expression)
        return {"result": result}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid Expression")
