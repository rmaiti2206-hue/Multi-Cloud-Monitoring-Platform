import boto3
def session_from_config(c):
    if c.get('role_arn'):
        sts=boto3.client('sts'); r=sts.assume_role(RoleArn=c['role_arn'],RoleSessionName='multicloud-monitor'); q=r['Credentials']; return boto3.Session(aws_access_key_id=q['AccessKeyId'],aws_secret_access_key=q['SecretAccessKey'],aws_session_token=q['SessionToken'],region_name=c.get('region','ap-south-1'))
    return boto3.Session(region_name=c.get('region','ap-south-1'))
