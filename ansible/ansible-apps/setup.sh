#!/bin/bash

set -e

docker-compose down || { echo "Failed to stop containers"; exit 1; }
docker-compose up -d || { echo "Failed to start containers"; exit 1; }
ansible -i hosts.ini all -m ping -u root || { echo "Failed to ping hosts"; exit 1; }
ansible-playbook -i hosts.ini playbook.yaml || { echo "Failed to run playbook"; exit 1; }
bash checker-apps.sh || { echo "Checker failed"; exit 1; }
