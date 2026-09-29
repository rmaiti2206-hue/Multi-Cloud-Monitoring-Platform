from fastapi import APIRouter
from app.services.aws_service import list_ec2
router=APIRouter(prefix="/aws",tags=["AWS"])
@router.get("/resources")
def resources(): return list_ec2()
