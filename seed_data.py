from db import SessionLocal, WebhookEvent, create_tables
from datetime import datetime, timedelta
import random

# Ensure tables exist
create_tables()

# Start DB session
db = SessionLocal()

# Clear existing events (optional)
db.query(WebhookEvent).delete()

# Generate 100 events
for i in range(1, 101):
    event = WebhookEvent(
        event_id=f"evt_{i:03}",
        user_id=f"user_{random.randint(1, 20)}",
        amount=round(random.uniform(10.0, 500.0), 2),
        timestamp=datetime.utcnow() - timedelta(days=random.randint(0, 30))
    )
    db.add(event)

db.commit()
db.close()

print("✅ Seeded 100 webhook events.")
