from fastapi import APIRouter
from datetime import datetime,timezone
router=APIRouter(prefix="/alerts",tags=["Alerts"])
@router.get("")
def alerts():
    return [{"id":1,"severity":"INFO","message":"Monitoring platform is running","time":datetime.now(timezone.utc).isoformat()}]
