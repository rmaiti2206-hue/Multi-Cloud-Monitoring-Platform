import json
from app.cloud.aws.client import session_from_config
from app.cloud.aws.ec2 import list_instances as aec2
from app.cloud.aws.s3 import list_buckets as as3
from app.cloud.aws.rds import list_databases as ards
from app.cloud.aws.iam import list_iam as aiam
from app.cloud.azure.client import clients as azclients
from app.cloud.azure.vm import list_vms
from app.cloud.azure.storage import list_storage
from app.cloud.gcp.client import clients as gcclients
from app.cloud.gcp.compute import list_instances as gcompute
from app.cloud.gcp.storage import list_buckets as gs3

def fetch(account,kind):
 c=json.loads(account.config_json or '{}'); p=account.provider.upper()
 if p=='AWS':
  s=session_from_config(c);r=c.get('region','ap-south-1')
  return aec2(s,r) if kind in ('all','ec2') else as3(s) if kind=='s3' else ards(s,r) if kind=='rds' else aiam(s) if kind=='iam' else []
 if p=='AZURE':
  x=azclients(c);return list_vms(x) if kind in ('all','vm') else list_storage(x) if kind=='storage' else []
 if p=='GCP':
  x=gcclients(c);return gcompute(x) if kind in ('all','compute') else gs3(x) if kind=='storage' else []
 return []
