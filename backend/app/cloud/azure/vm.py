def list_vms(c): return [{'provider':'Azure','id':x.name,'type':'Virtual Machine','status':x.provisioning_state or 'unknown','region':x.location} for x in c['compute'].virtual_machines.list_all()]
