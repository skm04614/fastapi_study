from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.domain.question import crud
from backend.domain.question.schema import Question

router = APIRouter(
    prefix="/question",
    tags=["question"]
)


@router.get("/list", response_model=list[Question])
def question_list(db: Session = Depends(get_db)):
    return crud.get_question_list(db)
