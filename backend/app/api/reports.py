from fastapi import APIRouter
router=APIRouter(prefix="/reports",tags=["Reports"])
@router.get("")
def report(): return {"resources":0,"healthy":0,"alerts":0,"generated":"live"}
