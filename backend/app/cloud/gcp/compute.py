def list_instances(c):
 out=[]
 for _,z in c['compute'].aggregated_list(project=c['project_id']):
  for x in z.instances or []: out.append({'provider':'GCP','id':x.name,'type':'Compute Engine','status':x.status,'region':x.zone.split('/')[-1]})
 return out
