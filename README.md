# ════════════════════════════════════════════════════════════
#  Annappa M — Portfolio  |  README.md
# ════════════════════════════════════════════════════════════

# DevOps Portfolio — Annappa M

A professional portfolio website built with **Python Flask**, featuring:
- Midnight dark theme with glassmorphism UI
- Typed.js animated hero titles
- Scroll-reveal animations
- Interactive experience timeline
- Downloadable PDF resume

## Project Structure

```
portfolio/
├── app.py                    # Flask application + data layer
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variable template
├── templates/
│   ├── layout.html           # Jinja2 base template
│   └── index.html            # Main landing page
└── static/
    ├── css/style.css         # Custom responsive CSS
    ├── js/main.js            # Scroll animations & UI logic
    └── assets/
        └── Annappa_M_DevOps_Resume.pdf   ← Add your PDF here
```

## Quick Start

```bash
# 1. Clone / download the project
cd portfolio

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set environment variables
cp .env.example .env
# Edit .env as needed

# 5. Add your resume PDF
cp /path/to/your/resume.pdf static/assets/Annappa_M_DevOps_Resume.pdf

# 6. Run locally
python app.py
# → Visit http://localhost:5000
```

## Production Deployment (Gunicorn)

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## Docker Deployment

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

## Customisation

All content data lives in `app.py` as Python dictionaries:
- `PROFILE` — name, tagline, bio, location
- `SKILLS` — skill categories + items
- `EXPERIENCE` — work history roles
- `PROJECTS` — featured projects
- `STATS` — hero statistics bar

Update these dicts and restart the server.

CICD 

# 🚀 DevOps Portfolio Website – Complete CI/CD Pipeline

This project demonstrates a **complete end-to-end DevOps CI/CD pipeline** that builds, pushes, and deploys a portfolio web application using modern DevOps tools.

The application is containerized using Docker, automated using Jenkins, stored in Docker Hub, and deployed into Kubernetes.

---

# 🧰 Tech Stack

* Git & GitHub
* Docker
* Docker Hub
* Jenkins
* Kubernetes (Docker Desktop)
* Python Flask
* kubectl

---

# 🏗 Architecture

Developer pushes code → GitHub → Jenkins Pipeline → Docker Image Build → Docker Hub → Kubernetes Deployment

```
Developer
   │
   ▼
GitHub Repository
   │
   ▼
Jenkins Pipeline
   │
   ▼
Docker Image Build
   │
   ▼
Docker Hub
   │
   ▼
Kubernetes Cluster
   │
   ▼
Running Application
```

---

# 📂 Project Structure

```
devops-portfolio-website
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
│
├── templates/
│   └── index.html
│
└── k8s/
    ├── deployment.yaml
    └── service.yaml
```

---

# ⚙️ Step 1 — Clone the Repository

```
git clone https://github.com/Ani-k8s/devops-portfolio-website.git

cd devops-portfolio-website
```

---

# ⚙️ Step 2 — Build Docker Image

Build the application container.

```
docker build -t anik8s/annappa-portfolio:v1 .
```

Check images

```
docker images
```

---

# ⚙️ Step 3 — Run Container Locally (Optional Test)

```
docker run -d -p 5000:5000 anik8s/annappa-portfolio:v1
```

Open browser

```
http://localhost:5000
```

---

# ⚙️ Step 4 — Push Image to Docker Hub

Login to Docker Hub

```
docker login
```

Push the image

```
docker push anik8s/annappa-portfolio:v1
```

Verify in Docker Hub repository.

---

# ⚙️ Step 5 — Install Jenkins using Docker

Run Jenkins container.

```
docker run -d \
--name jenkins \
-p 8080:8080 \
-p 50000:50000 \
-v jenkins_home:/var/jenkins_home \
-v /var/run/docker.sock:/var/run/docker.sock \
jenkins/jenkins:lts
```

Check container

```
docker ps
```

Open Jenkins

```
http://localhost:8080
```

Unlock Jenkins using the password

```
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Install suggested plugins.

---

# ⚙️ Step 6 — Configure Jenkins Pipeline

Create new job

```
New Item → Pipeline
```

Configure pipeline script.

Jenkinsfile example:

```
pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/Ani-k8s/devops-portfolio-website.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t anik8s/annappa-portfolio:v3 .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push anik8s/annappa-portfolio:v3'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
            }
        }

    }
}
```

Run pipeline.

---

# ⚙️ Step 7 — Enable Kubernetes

Using Docker Desktop.

```
Docker Desktop → Settings → Kubernetes → Enable Kubernetes
```

Check cluster

```
kubectl get nodes
```

Example output

```
docker-desktop   Ready   control-plane
```

---

# ⚙️ Step 8 — Deploy Application to Kubernetes

Create deployment

```
kubectl apply -f k8s/deployment.yaml
```

Create service

```
kubectl apply -f k8s/service.yaml
```

Check pods

```
kubectl get pods
```

Check services

```
kubectl get svc
```

Example output

```
portfolio-service   NodePort   30007
```

---

# 🌐 Step 9 — Access the Application

Open browser

```
http://localhost:30007
```

The portfolio application will be running inside Kubernetes.

---

# 🔁 CI/CD Workflow

Every time code is pushed to GitHub:

1. Jenkins detects the change
2. Jenkins clones the repository
3. Jenkins builds a Docker image
4. Image is pushed to Docker Hub
5. Kubernetes deployment updates the application

This provides **fully automated CI/CD deployment**.

---

# 📊 Kubernetes Resources Used

Deployment

* Manages pods
* Ensures application availability
* Handles scaling

Service

* Exposes the application
* Allows external access

---

# 🧪 Useful Commands

Check running containers

```
docker ps
```

Check Kubernetes pods

```
kubectl get pods
```

Check services

```
kubectl get svc
```

Delete deployment

```
kubectl delete deployment annappa-portfolio
```

Delete service

```
kubectl delete service portfolio-service
```

---

# 🎯 Key DevOps Concepts Demonstrated

CI/CD Pipeline
Containerization
Image Registry
Infrastructure Automation
Kubernetes Orchestration
Continuous Deployment

---

# 👨‍💻 Author

Annappa
DevOps Engineer Portfolio Project

GitHub
https://github.com/Ani-k8s

---

# ⭐ Future Improvements

* Helm charts
* Kubernetes Ingress
* Horizontal Pod Autoscaler
* Prometheus & Grafana monitoring
* GitHub Webhooks
* Terraform infrastructure

---

# 🏁 Conclusion

This project demonstrates a **complete real-world DevOps workflow** from code commit to production deployment using industry-standard tools.

