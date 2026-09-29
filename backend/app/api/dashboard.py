from fastapi import APIRouter
router=APIRouter(prefix="/dashboard",tags=["Dashboard"])
@router.get("/summary")
def summary():
    return {"total_resources":0,"healthy_resources":0,"alerts":0,"accounts":3,
    "providers":{
      "AWS":{"resources":0,"healthy":0,"status":"Not Configured"},
      "Azure":{"resources":0,"healthy":0,"status":"Not Configured"},
      "GCP":{"resources":0,"healthy":0,"status":"Not Configured"}}}
