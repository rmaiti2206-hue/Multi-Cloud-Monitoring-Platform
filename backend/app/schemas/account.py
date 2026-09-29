from pydantic import BaseModel
class AccountCreate(BaseModel):
 provider:str;name:str;role_arn:str='';region:str='ap-south-1';subscription_id:str='';tenant_id:str='';client_id:str='';client_secret:str='';project_id:str=''
