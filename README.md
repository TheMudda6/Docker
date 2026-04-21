🚀 Docker Projects Portfolio

This repository showcases my hands-on projects building containerised applications using Docker.

📦 Projects
🔹 Flask + Redis + NGINX (Load Balanced Application)

A scalable multi-container application built with Docker Compose.

Architecture:
Browser → NGINX → Flask (multiple instances) → Redis

Tech stack:

Python (Flask)
Redis
NGINX
Docker & Docker Compose

Features:

/ → Welcome page
/count → Tracks visits using Redis
/reset → Resets the counter

👉 View Project

🔹 Hello Flask (Starter Project)

A simple Flask app containerised using Docker.

👉 View Project

🧠 Skills Demonstrated
Containerisation using Docker
Writing Dockerfiles
Multi-container orchestration with Docker Compose
Container networking (service-to-service communication)
Environment variables for configuration
Persistent storage using Docker volumes
Reverse proxy & load balancing using NGINX
Debugging container issues
🎯 Key Learnings
Containers communicate via service names, not localhost
Port mapping is required for external access
Docker Compose simplifies multi-service applications
Real-world systems require multiple services working together
