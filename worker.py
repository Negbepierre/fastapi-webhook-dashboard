import time
from db import SessionLocal, WebhookEvent

def process_event(event_data):
    print(f"Processing event {event_data['event_id']}...")

    time.sleep(2)  # simulate delay

    try:
        db = SessionLocal()
        webhook_event = WebhookEvent(
            event_id=event_data['event_id'],
            user_id=event_data['user_id'],
            amount=event_data['amount'],
            status=event_data['status']
        )
        db.add(webhook_event)
        db.commit()
        db.close()

        print(f"✅ Stored event {event_data['event_id']} in database")

    except Exception as e:
        print(f"❌ Error storing event {event_data['event_id']}: {e}")
