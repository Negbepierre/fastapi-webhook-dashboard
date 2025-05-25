from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db import SessionLocal, WebhookEvent, create_tables
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Create DB table
create_tables()

@app.post("/webhook")
async def receive_webhook(request: Request):
    payload = await request.json()
    db = SessionLocal()

    try:
        event = WebhookEvent(
            event_id=payload["event_id"],
            user_id=payload["user_id"],
            amount=payload["amount"],
            timestamp=datetime.utcnow()
        )
        db.add(event)
        db.commit()
        db.refresh(event)
        return {"status": "success", "data": payload}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
    finally:
        db.close()

@app.get("/dashboard", response_class=HTMLResponse)
def read_dashboard(request: Request):
    db = SessionLocal()
    events = db.query(WebhookEvent).all()
    return templates.TemplateResponse("dashboard.html", {"request": request, "events": events})
