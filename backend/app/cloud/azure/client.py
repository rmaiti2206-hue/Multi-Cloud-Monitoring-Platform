from azure.identity import DefaultAzureCredential,ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
def clients(c):
 cred=ClientSecretCredential(c['tenant_id'],c['client_id'],c['client_secret']) if c.get('tenant_id') and c.get('client_id') and c.get('client_secret') else DefaultAzureCredential()
 sub=c['subscription_id'];return {'resource':ResourceManagementClient(cred,sub),'compute':ComputeManagementClient(cred,sub)}
