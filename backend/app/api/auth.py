from fastapi import APIRouter,HTTPException
from app.schemas.auth import LoginRequest
from app.utils.security import create_token
router=APIRouter(prefix="/auth",tags=["Authentication"])
@router.post("/login")
def login(data:LoginRequest):
    if data.email=="admin@example.com" and data.password=="admin123":
        return {"access_token":create_token(data.email),"token_type":"bearer"}
    raise HTTPException(status_code=401,detail="Invalid credentials")
