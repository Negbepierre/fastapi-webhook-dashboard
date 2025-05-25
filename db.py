from sqlalchemy import create_engine, Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# PostgreSQL connection URL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:dreiya1968@localhost:5432/webhook_db"

# Create SQLAlchemy engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Define base class for models
Base = declarative_base()

# Define WebhookEvent model
class WebhookEvent(Base):
    __tablename__ = "webhook_events"
    event_id = Column(String, primary_key=True, index=True)
    user_id = Column(String)
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Create table
def create_tables():
    Base.metadata.create_all(bind=engine)
