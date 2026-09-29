import boto3
def list_ec2(region="ap-south-1"):
    try:
        c=boto3.client("ec2",region_name=region)
        out=[]
        for r in c.describe_instances().get("Reservations",[]):
            for x in r.get("Instances",[]):
                out.append({"id":x.get("InstanceId"),"type":"EC2","status":x.get("State",{}).get("Name"),"region":region})
        return out
    except Exception:
        return []
