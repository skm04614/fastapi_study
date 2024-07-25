from typing import Type

from sqlalchemy.orm import Session

from backend.models.question import Question


def get_question_list(db: Session) -> list[Type[Question]]:
    return db.query(Question).order_by(Question.created_date.desc()).all()
