from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from backend.database import Base
from backend.models.question import Question


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    created_date = Column(DateTime,
                          nullable=False,
                          default=func.now())
    question_id = Column(Integer, ForeignKey("question.id"))
    quesiton = relationship(Question, backref="answers")
