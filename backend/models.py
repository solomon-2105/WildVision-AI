from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class Detection(Base):

    __tablename__ = "detections"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String(255))

    predicted_class = Column(String(100))

    confidence = Column(Float)

    image_path = Column(String(255))

    created_at = Column(DateTime, default=datetime.utcnow)