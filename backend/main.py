from pathlib import Path

from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="Starter App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter(prefix="/api")


class LoginRequest(BaseModel):
    id_token: str


@app.get("/health")
async def health():
    return {"status": "ok"}


@api_router.get("/subtract")
async def subtract(a: float, b: float):
    result = a - b

    return {"operation": "subtraction", "result": result}


@api_router.post("/login")
async def login(payload: LoginRequest):
    if not payload.id_token:
        raise HTTPException(status_code=400, detail="Google ID token is required")

    return {"message": "Login successful", "authenticated": True}


# class that contains parameters needed when user uses multiplication endpoints
class Numbers(BaseModel):
    number1: float
    number2: float


@api_router.post("/multiply")
async def multiply(num: Numbers):
    return {"result": num.number1 * num.number2}


# Register API routes FIRST
app.include_router(api_router)

# Mount the frontend LAST
frontend_dir = Path(__file__).resolve().parent.parent / "frontend"

app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")
@api_router.get("/logarithm")
async def logarithm(number: float, base: float = 10):
    if number <= 0:
        raise HTTPException(
            status_code=400,
            detail="Number must be greater than 0"
        )

    if base <= 0 or base == 1:
        raise HTTPException(
            status_code=400,
            detail="Base must be greater than 0 and cannot be 1"
        )

    result = math.log(number, base)

    return {
        "operation": "logarithm",
        "number": number,
        "base": base,
        "result": result
    }