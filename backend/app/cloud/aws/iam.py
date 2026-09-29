def list_iam(session):
 c=session.client('iam');o=[]
 for x in c.list_users().get('Users',[]): o.append({'provider':'AWS','id':x['UserName'],'type':'IAM User','status':'active','region':'global'})
 for x in c.list_roles().get('Roles',[]): o.append({'provider':'AWS','id':x['RoleName'],'type':'IAM Role','status':'active','region':'global'})
 return o
