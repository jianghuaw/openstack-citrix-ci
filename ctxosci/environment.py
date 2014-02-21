def get_environment(change_ref):
    env  = 'ZUUL_URL=https://review.openstack.org'
    env += ' ZUUL_REF=%s' % change_ref
    env += ' PYTHONUNBUFFERED=true'
    env += ' DEVSTACK_GATE_TEMPEST=1'
    env += ' DEVSTACK_GATE_TEMPEST_FULL=1'
    env += ' DEVSTACK_GATE_VIRT_DRIVER=xenapi'
    # Set gate timeout to 3 hours
    env += ' DEVSTACK_GATE_TIMEOUT=180'
    env += ' APPLIANCE_NAME=devstack'
    env += ' ENABLED_SERVICES=g-api,g-reg,key,n-api,n-crt,n-obj,n-cpu,n-sch,horizon,mysql,rabbit,sysstat,dstat,pidstat,s-proxy,s-account,s-container,s-object,n-cond'
    return env.split()
