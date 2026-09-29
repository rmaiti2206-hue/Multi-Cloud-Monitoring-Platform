from fastapi import APIRouter
from app.services.azure_service import list_resources

router = APIRouter(
    prefix="/azure",
    tags=["Azure"]
)

@router.get("/resources")
def resources():
    return list_resources()