from fastapi import FastAPI
from app.api.v1.api import api_router
from fastapi.responses import RedirectResponse
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)
app.include_router(api_router, prefix="/api/v1")


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/api/v1/calculator")
