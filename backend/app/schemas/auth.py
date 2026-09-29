from pydantic import BaseModel,EmailStr
class LoginRequest(BaseModel):
    email: str
    password: str
class Token(BaseModel):
    access_token:str
    token_type:str="bearer"
