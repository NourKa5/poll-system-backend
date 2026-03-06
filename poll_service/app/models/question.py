from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.database import Base

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(500), nullable=False)
    option_a = Column(String(200), nullable=False)
    option_b = Column(String(200), nullable=False)
    option_c = Column(String(200), nullable=False)
    option_d = Column(String(200), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    answers = relationship("Answer", back_populates="question", cascade="all, delete")
