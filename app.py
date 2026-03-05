"""
Portfolio Website - Annappa M | DevOps Engineer
Flask application entry point
"""

from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-prod')


# ── Data Layer ──────────────────────────────────────────────────────────────

PROFILE = {
    "name": "Annappa M",
    "title": "DevOps Engineer",
    "tagline": "DevOps Engineer | 8.5 Years of Enterprise IT Experience",
    "location": "Davanagere, Karnataka",
    "email": "annappa.m@example.com",
    "github": "https://github.com/annappa-m",
    "linkedin": "https://linkedin.com/in/annappa-m",
    "about": (
        "I am a seasoned IT professional with a unique 8.5-year trajectory. "
        "Starting in Manual Testing and L2 Production Support at Wipro, I developed "
        "a deep 'production-first' mindset. Today, I leverage that experience to build "
        "rock-solid CI/CD pipelines, containerized environments, and automated "
        "infrastructures. I don't just build pipelines — I build stability."
    ),
    "typed_strings": [
        "DevOps Engineer",
        "Cloud Infrastructure Architect",
        "CI/CD Pipeline Builder",
        "Kubernetes Enthusiast",
        "Automation Specialist",
    ],
}

SKILLS = [
    {
        "category": "Orchestration",
        "icon": "⚙️",
        "tools": ["Kubernetes", "Minikube", "Helm", "Container Orchestration"],
        "color": "#00d4ff",
    },
    {
        "category": "Cloud & IaC",
        "icon": "☁️",
        "tools": ["AWS EC2", "AWS IAM", "Terraform", "Infrastructure as Code"],
        "color": "#ff6b35",
    },
    {
        "category": "CI/CD & Containers",
        "icon": "🔁",
        "tools": ["Jenkins", "Docker", "Docker Compose", "Pipeline Automation"],
        "color": "#7c3aed",
    },
    {
        "category": "Version Control",
        "icon": "🌿",
        "tools": ["Git", "GitHub", "GitFlow", "Code Reviews"],
        "color": "#10b981",
    },
    {
        "category": "Operating Systems",
        "icon": "🐧",
        "tools": ["Linux (Ubuntu)", "WSL2", "Bash Scripting", "Shell Automation"],
        "color": "#f59e0b",
    },
    {
        "category": "Monitoring & Support",
        "icon": "📊",
        "tools": ["L2 Production Support", "Incident Management", "Log Analysis", "SLA Management"],
        "color": "#ec4899",
    },
]

EXPERIENCE = [
    {
        "company": "Wipro Technologies",
        "duration": "8.5 Years",
        "logo_initial": "W",
        "roles": [
            {
                "title": "Senior Project Engineer – DevOps / Deployment",
                "project": "Holmes Endpoint Solution",
                "period": "2021 – Present",
                "type": "devops",
                "highlights": [
                    "Designed and implemented end-to-end CI/CD pipelines using Jenkins and Docker",
                    "Containerized microservices and managed deployments via Kubernetes (Minikube)",
                    "Provisioned cloud infrastructure on AWS using Terraform (IaC)",
                    "Automated deployment workflows reducing release cycle time by 60%",
                    "Managed IAM roles, EC2 instances, and cloud security policies",
                ],
            },
            {
                "title": "Senior Project Engineer – L2 Production Support",
                "project": "WCCLG (Wipro Client)",
                "period": "2018 – 2021",
                "type": "support",
                "highlights": [
                    "Provided L2 production support for enterprise-grade applications",
                    "Triaged and resolved critical incidents within SLA windows",
                    "Collaborated with Dev teams to implement permanent bug fixes",
                    "Developed deep understanding of production systems and failure modes",
                    "Mentored junior support engineers on incident response protocols",
                ],
            },
            {
                "title": "Project Engineer – Manual Testing",
                "project": "OneForce Platform",
                "period": "2015 – 2018",
                "type": "testing",
                "highlights": [
                    "Executed comprehensive manual test plans for enterprise platform",
                    "Authored detailed test cases and defect reports in JIRA",
                    "Performed regression, integration, and UAT testing cycles",
                    "Built foundational 'quality-first' engineering mindset",
                    "Collaborated cross-functionally with developers and business analysts",
                ],
            },
        ],
    }
]

PROJECTS = [
    {
        "title": "Automated CI/CD Pipeline",
        "subtitle": "Jenkins · Docker · Kubernetes",
        "description": (
            "A production-grade Jenkins-based workflow for Python applications. "
            "Source code triggers automated build, test, and containerization via Docker, "
            "with orchestrated rolling deployments to a Kubernetes cluster."
        ),
        "tags": ["Jenkins", "Docker", "Kubernetes", "Python", "GitOps"],
        "icon": "🚀",
        "color": "#00d4ff",
        "github": "#",
        "highlights": [
            "Automated build → test → containerize → deploy lifecycle",
            "Kubernetes rolling updates with zero-downtime deployments",
            "Integrated health checks and automatic rollback triggers",
        ],
    },
    {
        "title": "AWS Infrastructure with Terraform",
        "subtitle": "Terraform · AWS · IaC",
        "description": (
            "Fully declarative AWS infrastructure provisioned via Terraform. "
            "Covers VPC setup, EC2 instances, IAM roles, security groups, "
            "and remote state management — all version-controlled."
        ),
        "tags": ["Terraform", "AWS EC2", "AWS IAM", "VPC", "IaC"],
        "icon": "☁️",
        "color": "#ff6b35",
        "github": "#",
        "highlights": [
            "Modular Terraform code for reusable infrastructure components",
            "Remote state with S3 backend and DynamoDB state locking",
            "Principle of least privilege IAM policies",
        ],
    },
    {
        "title": "Linux System Automation Suite",
        "subtitle": "Bash · Shell Scripting · Linux",
        "description": (
            "A collection of production-hardened Bash scripts for Linux system "
            "administration — automated log rotation, disk monitoring alerts, "
            "service health checks, and scheduled maintenance tasks."
        ),
        "tags": ["Bash", "Linux", "Cron", "Shell", "Monitoring"],
        "icon": "🐧",
        "color": "#10b981",
        "github": "#",
        "highlights": [
            "Real-time disk and CPU threshold alerting via email/Slack",
            "Automated log archival with configurable retention policies",
            "Service watchdog with auto-restart and notification logic",
        ],
    },
]

STATS = [
    {"value": "8.5", "unit": "Years", "label": "Industry Experience"},
    {"value": "3", "unit": "+", "label": "Major Enterprises Served"},
    {"value": "60", "unit": "%", "label": "Faster Release Cycles"},
    {"value": "100", "unit": "%", "label": "Production Uptime Focus"},
]


# ── Routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=PROFILE,
        skills=SKILLS,
        experience=EXPERIENCE,
        projects=PROJECTS,
        stats=STATS,
    )


@app.route("/resume")
def resume():
    """Serve the PDF resume for download."""
    try:
        return send_from_directory(
            "static/assets",
            "Annappa_M_DevOps_Resume.pdf",
            as_attachment=True,
            download_name="Annappa_M_DevOps_Resume.pdf",
        )
    except FileNotFoundError:
        # Graceful fallback if PDF not yet uploaded
        return render_template("index.html", profile=PROFILE, skills=SKILLS,
                               experience=EXPERIENCE, projects=PROJECTS,
                               stats=STATS, resume_missing=True)
@app.route("/health")
def health():
    """Health check endpoint for deployment monitoring."""
    return {"status": "healthy", "service": "portfolio"}, 200


# ── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV", "production") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
