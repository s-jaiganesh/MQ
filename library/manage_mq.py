#!/usr/bin/python
import json

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': ''
}

DOCUMENTATION = '''
---
module: manage_mq
short_description: Create MQ Queue

version_added: "1.0"

description:
    - 

author:
    - 
'''

EXAMPLES = '''
- name: Create Queue
  manage_mq:
    MQMGR: "{{ mqmgr }}"
    QNAME: "{{ qname }}"
    MAXDEPTH: "{{ maxdepth }}"
    DESCR: "{{ desc }}"
    MAXMSGL: "{{ maxlen }}"
    state: "present"
    
'''

from ansible.module_utils.basic import AnsibleModule, load_platform_subclass

def _create_queue(module, QNAME, MAXDEPTH, DESC, MAXLEN, MQMGR):

    cmd = "'%s' '%s' %s '%s' %s '%s' %s '%s' %s '%s' %s" % ('echo', 'DEFINE QL(', QNAME, ') MAXDEPTH(', MAXDEPTH, ') DESCR(', DESC, ') MAXMSGL(', MAXLEN, ') | runmqsc', MQMGR)
    rc, out, err = module.run_command(cmd, encoding=None)
    if rc is 0:
        msg = ("Successfully executed %s command" % cmd)
        result = { 'stdout':out, 'stderr':err, 'rc':rc, 'changed':True }
        module.exit_json(**result)
    else:
        msg = ("Failed to run %s command" % cmd)
        result = { 'stdout':out, 'stderr':err, 'rc':rc, 'changed':False }
        module.exit_json(**result)
    
def main():
    module = AnsibleModule(
        argument_spec=dict(
            QNAME=dict(type='str', required=False),
            MAXDEPTH=dict(type='int', required=False),
            DESC=dict(type='str', required=False),
            MAXLEN=dict(type='int', required=False),            
            MQMGR=dict(type='str', required=False)  
            state=dict(type='str', required=False, choices=['present', 'absent']),
        ),
        supports_check_mode=True,
    )
    if module.check_mode:
        module.exit_json(**result)

    QNAME = module.params['QNAME']
    MAXDEPTH = module.params['MAXDEPTH']
    DESC = module.params['DESC']
    MAXLEN = module.params['MAXLEN']
    MQMGR = module.params['MQMGR']
    state = module.params['state']

    if state == 'present':
        _create_queue(module, QNAME, MAXDEPTH, DESC, MAXLEN, MQMGR)   
    else:
        module.fail_json(msg = "Invalid input")

if __name__ == '__main__':
    main()
