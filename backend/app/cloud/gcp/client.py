from google.cloud import compute_v1,storage
def clients(c): return {'project_id':c['project_id'],'compute':compute_v1.InstancesClient(),'storage':storage.Client(project=c['project_id'])}
