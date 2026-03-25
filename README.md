# HostelPulse FastAPI Starter

This is a basic FastAPI backend starter for HostelPulse aligned with TRD endpoint paths.

## Route style

Routes follow TRD-style resource paths:

- /api/v1/auth/...
- /api/v1/students/...
- /api/v1/attendance/...
- /api/v1/leaves/...
- /api/v1/grievances/...
- /api/v1/messages/...
- /api/v1/payments/...
- /api/v1/notifications/...
- /api/v1/rooms/...

Allowed roles:

- student
- warden
- guard
- staff

Access is controlled per endpoint using the request header:

- X-Role: student | warden | guard | staff

## Run locally

1. Create virtual environment:

   python -m venv .venv

2. Activate it:

   Windows (PowerShell): .venv\\Scripts\\Activate.ps1

3. Install dependencies:

   pip install -r requirements.txt

4. Run server:

   uvicorn app.main:app --reload

5. Open docs:

   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc

## Example endpoints

- GET /api/v1/auth/me (X-Role required)
- POST /api/v1/attendance/generate-qr (X-Role: guard)
- POST /api/v1/attendance/scan (X-Role: student)
- POST /api/v1/leaves (X-Role: student)
- PUT /api/v1/leaves/{leave_id}/approve (X-Role: warden)
- GET /api/v1/students (X-Role: warden)

## Deploy on Render

### Option A: Manual setup

1. Push this project to GitHub.
2. Go to Render Dashboard > New + > Web Service.
3. Connect your GitHub repository.
4. Use these settings:
   - Environment: Python
   - Build Command: pip install -r requirements.txt
   - Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
   - Python version: 3.11.9
5. Click Create Web Service.
6. Wait for deploy and test:
   - https://<your-render-service>.onrender.com/health

### Option B: Blueprint deployment

1. Keep render.yaml in repository root.
2. In Render, choose New + > Blueprint.
3. Select repository.
4. Render reads render.yaml and creates service automatically.

## Attach your own domain (DigitalPlat registrar)

After your Render service is live:

1. In Render: Service > Settings > Custom Domains > Add Custom Domain.
2. Add your domain name (example: api.yourdomain.com).
3. Render will show DNS records to add.

Use one of these common setups:

### Subdomain setup (recommended)

If using api.yourdomain.com, add at DigitalPlat DNS:

- Type: CNAME
- Host/Name: api
- Value/Target: <your-render-service>.onrender.com
- TTL: 300 or default

### Root domain setup (yourdomain.com)

Render usually gives A records or ALIAS/ANAME instructions. Add exactly what Render shows.

4. Save DNS changes in DigitalPlat panel.
5. Wait for DNS propagation (usually 5-30 minutes, can be up to 24 hours).
6. Back in Render, click Verify.
7. Once verified, Render provisions SSL certificate automatically.

## Troubleshooting

- 404 on domain: confirm DNS target exactly matches Render value.
- SSL pending: wait for DNS propagation, then retry verify.
- Deploy failed: check Render logs for build/start command errors.
