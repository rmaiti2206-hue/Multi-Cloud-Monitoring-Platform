from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.db import Base,engine
from app.api import auth,dashboard,aws,azure,gcp,resources,metrics,alerts,accounts,users,reports
Base.metadata.create_all(bind=engine)
app=FastAPI(title="Multi-Cloud Monitoring Platform",version="1.0.0")
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:5173"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
for r in [auth.router,dashboard.router,aws.router,azure.router,gcp.router,resources.router,metrics.router,alerts.router,accounts.router,users.router,reports.router]: app.include_router(r,prefix="/api")
@app.get("/")
def root(): return {"name":"Multi-Cloud Monitoring Platform","status":"running"}
@app.get("/health")
def health(): return {"status":"healthy"}
