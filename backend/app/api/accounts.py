from fastapi import APIRouter
router=APIRouter(prefix="/accounts",tags=["Cloud Accounts"])
@router.get("")
def accounts():
    return [{"provider":"AWS","name":"Authorized AWS Account","status":"Not Configured"},
            {"provider":"Azure","name":"Authorized Azure Subscription","status":"Not Configured"},
            {"provider":"GCP","name":"Authorized GCP Project","status":"Not Configured"}]
