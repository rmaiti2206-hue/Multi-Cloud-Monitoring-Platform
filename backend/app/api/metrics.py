from fastapi import APIRouter
router=APIRouter(prefix="/metrics",tags=["Metrics"])
@router.get("/overview")
def overview(): return {"cpu":48,"memory":61,"network_mbps":28,"storage":67}
