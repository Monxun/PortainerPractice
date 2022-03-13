
# CREATE INSTANCES
`$ ansible-playbook -e instances="test-1 test-2" gce-instances-create.yml`

# DELETE INSTANCES
`$ ansible-playbook -e instances="test-1 test-2" gce-instances-delete.yml`