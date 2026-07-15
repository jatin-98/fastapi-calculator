from fastapi import FastAPI
from app.api.v1.api import api_router
from fastapi.responses import RedirectResponse
from app.core.config import settings
from fastapi.staticfiles import StaticFiles

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)
app.include_router(api_router, prefix="/api/v1")

app.mount("/", StaticFiles(directory="app/static", html=True))

# @app.get("/", include_in_schema=False)
# def root():
#     return RedirectResponse(url="/api/v1/calculator")
