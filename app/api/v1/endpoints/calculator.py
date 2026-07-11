from fastapi.routing import APIRouter
from app.services.calculator import perform_calculation
from app.schemas.calculator import CalculatorRequest, CalculatorResponse

router = APIRouter()


@router.post("/", response_model=CalculatorResponse)
def calculate(request: CalculatorRequest):
    result = perform_calculation(request.a, request.b, request.operation)
    return {"result": result}
