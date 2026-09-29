def list_buckets(c): return [{'provider':'GCP','id':x.name,'type':'Cloud Storage','status':'available','region':x.location} for x in c['storage'].list_buckets()]
