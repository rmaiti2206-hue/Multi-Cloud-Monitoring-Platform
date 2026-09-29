from sqlalchemy import Column,Integer,String
from app.database.db import Base
class CloudAccount(Base):
    __tablename__="cloud_accounts"
    id=Column(Integer,primary_key=True)
    provider=Column(String)
    name=Column(String)
    status=Column(String,default="Not Configured")
