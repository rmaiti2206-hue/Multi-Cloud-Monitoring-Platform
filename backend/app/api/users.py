from fastapi import APIRouter
router=APIRouter(prefix="/users",tags=["Users"])
@router.get("")
def users():
    return [{"id":1,"email":"admin@example.com","role":"admin","status":"Active","last_login":"Demo"}]
