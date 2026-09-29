# Multi-Cloud Monitoring Platform

A full-stack MCA major-project starter implementation for authorized monitoring of AWS, Azure and GCP.

## Stack
- Frontend: React + Vite
- Backend: FastAPI
- Database: SQLite by default (easy local setup)
- Metrics: Prometheus
- Visualization: Grafana
- Cloud SDK adapters: boto3, azure-identity/management SDKs, google-cloud SDKs
- Docker Compose

## Important
Cloud credentials are NOT included. Use `.env.example` and configure only authorized accounts/resources.

## Quick Start
### Backend
```powershell
cd backend
python -m venv venv
.env\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend
```powershell
cd frontend
npm install
npm run dev
```

### Monitoring stack
```powershell
docker compose up -d prometheus grafana
```

Frontend: http://localhost:5173
API docs: http://localhost:8000/docs
Prometheus: http://localhost:9090
Grafana: http://localhost:3000

See `docs/SETUP.md` for cloud configuration.
