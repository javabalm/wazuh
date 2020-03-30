#!/usr/bin/env bash

sed -i 's,"mode": \("white"\|"black"\),"mode": "white",g' /var/ossec/framework/python/lib/python3.7/site-packages/api-4.0.0-py3.7.egg/api/configuration.py
sed -i "s:    # policies = RBAChecker.run_testing():    policies = RBAChecker.run_testing():g" /var/ossec/framework/python/lib/python3.7/site-packages/wazuh-3.12.0-py3.7.egg/wazuh/rbac/preprocessor.py
permissions='[{"actions": ["sca:read"],"resources": ["agent:id:000", "agent:group:group2"],"effect":"allow"}]'
awk -v var="${permissions}" '{sub(/testing_policies = \[\]/, "testing_policies = " var)}1' /var/ossec/framework/python/lib/python3.7/site-packages/wazuh-3.12.0-py3.7.egg/wazuh/rbac/auth_context.py >> /var/ossec/framework/python/lib/python3.7/site-packages/wazuh-3.12.0-py3.7.egg/wazuh/rbac/auth_context1.py
cat /var/ossec/framework/python/lib/python3.7/site-packages/wazuh-3.12.0-py3.7.egg/wazuh/rbac/auth_context1.py > /var/ossec/framework/python/lib/python3.7/site-packages/wazuh-3.12.0-py3.7.egg/wazuh/rbac/auth_context.py
