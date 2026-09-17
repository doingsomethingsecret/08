# TKXEL Assignment 08

Flask + PostgreSQL app deployed on a VM using Vagrant and Ansible.

## Stack

- Flask (Python)
- PostgreSQL 15
- Docker / Docker Compose
- Vagrant (VirtualBox)
- Ansible

## Project Structure

- `app/` — Flask app and Dockerfile
- `ansible/` — Ansible playbook and roles
- `nginx-local/` — local nginx config
- `Vagrantfile` — VM definition
- `docker-compose.yml` — app and DB services

## Quick Start

```bash
vagrant up
vagrant ssh
cd /vagrant
docker compose up -d
```

App: http://localhost:5000/  
DB check: http://localhost:5000/db-check
