# FastAPI Webhook Queue Simulation

This project demonstrates how a webhook system can be built using FastAPI, simulating how platforms like Stripe send events to your backend and how you can queue and process those events asynchronously.

## 🚀 Live Demo  
👉 [Live Webhook App](https://your-app-name.onrender.com/webhook) *(replace this after deployment)*

---

## 📦 What It Does

- Accepts webhook POST requests at `/webhook`
- Immediately queues the request for background processing
- Uses FastAPI’s `BackgroundTasks` to simulate a job worker
- Prints status logs showing success/failure of event processing

---

## 📁 Sample Payload

Test it using Postman or curl:

```json
{
  "event_id": "evt_001",
  "amount": 49.99,
  "user_id": "user_123",
  "status": "succeeded"
}
