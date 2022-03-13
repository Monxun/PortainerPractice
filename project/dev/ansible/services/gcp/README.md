
# CREATE INSTANCES
`ansible-playbook -e instances="test-1 test-2 test-3" k8-instances-create.yml`

# DELETE INSTANCES
`ansible-playbook -e instances="test-1 test-2 test-3" k8-instances-delete.yml`