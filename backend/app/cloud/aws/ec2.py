def list_instances(session,region):
    out=[]
    for r in session.client('ec2',region_name=region).describe_instances().get('Reservations',[]):
        for x in r.get('Instances',[]): out.append({'provider':'AWS','id':x['InstanceId'],'type':'EC2','status':x.get('State',{}).get('Name','unknown'),'region':region})
    return out
