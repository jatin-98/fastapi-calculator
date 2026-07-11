from fastapi.routing import APIRouter
from app.services.calculator import perform_calculation
from app.schemas.calculator import CalculatorRequest, CalculatorResponse
from fastapi import HTTPException

router = APIRouter()


@router.post("/", response_model=CalculatorResponse)
def calculate(request: CalculatorRequest):
    try:
        result = perform_calculation(request.a, request.b, request.operation)
        return {"result": result}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid operation")
