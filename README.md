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
