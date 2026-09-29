def list_buckets(session): return [{'provider':'AWS','id':x['Name'],'type':'S3','status':'available','region':'global'} for x in session.client('s3').list_buckets().get('Buckets',[])]
