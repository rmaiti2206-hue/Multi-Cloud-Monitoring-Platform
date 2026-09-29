from fastapi import APIRouter
from app.services.gcp_service import list_resources

router = APIRouter(
    prefix="/gcp",
    tags=["GCP"]
)

@router.get("/resources")
def resources():
    return list_resources()