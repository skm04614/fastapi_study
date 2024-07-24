from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.domain.question import question_crud

router = APIRouter(
    prefix="/question",
    tags=["question"]
)


@router.get("/list")
def question_list(db: Session = Depends(get_db)):
    return question_crud.get_question_list(db)
