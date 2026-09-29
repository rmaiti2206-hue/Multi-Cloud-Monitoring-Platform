from fastapi import Depends,HTTPException
from fastapi.security import HTTPBearer
from app.utils.security import decode_token
bearer=HTTPBearer()
def current_user(c=Depends(bearer)):
 try:return decode_token(c.credentials)
 except Exception:raise HTTPException(401,'Invalid or expired token')
