# Docker Projects Portfolio

Hands-on Docker and containerisation projects focused on building scalable multi-container applications, container networking, orchestration, and reverse proxy architectures.

---

# Featured Projects

## Flask + Redis + NGINX — Multi-Container Application

A scalable multi-container application built using Docker Compose with NGINX acting as a reverse proxy and Redis providing shared application state.

### Architecture

Browser → NGINX → Flask (Multiple Instances) → Redis

### Technologies Used

- Python (Flask)
- Redis
- NGINX
- Docker
- Docker Compose

### Features

- `/` → Welcome page
- `/count` → Tracks visits using Redis
- `/reset` → Resets the counter

### Skills Demonstrated

- Multi-container orchestration
- Docker Compose workflows
- Container networking
- Reverse proxy configuration
- Load balancing concepts
- Persistent storage using Docker volumes
- Service-to-service communication
- Debugging container issues

### Key Learnings

- Containers communicate using service names rather than localhost
- Port mapping is required for external access
- Docker Compose simplifies multi-service deployments
- Real-world applications rely on multiple interconnected services

Project:  
:contentReference[oaicite:0]{index=0}

---

## Hello Flask — Starter Container Project

A simple Flask application containerised using Docker to demonstrate the fundamentals of Docker images, Dockerfiles, and container execution.

### Skills Demonstrated

- Writing Dockerfiles
- Building Docker images
- Running containers
- Port mapping
- Basic containerisation workflows

Project:  
:contentReference[oaicite:1]{index=1}
