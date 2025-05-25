# 📬 FastAPI Webhook Dashboard

A FastAPI-based application that receives webhook events, stores them in a PostgreSQL database, and visualizes them on a Bootstrap-styled HTML dashboard.

## 🔧 Features

- FastAPI backend with `/webhook` POST endpoint.
- Stores incoming JSON events into PostgreSQL.
- Displays events in a Bootstrap dashboard at `/dashboard`.
- Queue worker setup ready for background jobs (e.g., Redis + RQ).
- Includes seeding script for mock events.

## 📦 Tech Stack

- **FastAPI** + **SQLAlchemy**
- **PostgreSQL** (via psycopg2)
- **Redis + RQ** (for background jobs)
- **Bootstrap** (via CDN)
- **Jinja2 Templates**

## 🚀 Quickstart

1. **Clone repo** and create a virtual environment:
   ```bash
   git clone https://github.com/your-username/fastapi-webhook-dashboard.git
   cd fastapi-webhook-dashboard
   python3 -m venv venv && source venv/bin/activate
2 Install dependencies: pip install -r requirements.txt

3 Configure your PostgreSQL credentials in db.py.

4 Run the app:
  uvicorn main:app --reload
5 Send sample webhook:
  Use Postman to POST http://127.0.0.1:8000/webhook with JSON:

json
Copy
Edit
{
  "event_id": "evt_001",
  "user_id": "user_123",
  "amount": 59.99
}
6 View dashboard:
Open http://127.0.0.1:8000/dashboard
