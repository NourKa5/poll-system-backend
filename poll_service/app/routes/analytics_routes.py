from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.controllers import analytics_controller

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/questions/{question_id}/option-counts")
def option_counts(question_id: int, db: Session = Depends(get_db)):
    return analytics_controller.get_option_counts_per_question(question_id, db)

@router.get("/questions/{question_id}/total-answers")
def total_answers(question_id: int, db: Session = Depends(get_db)):
    return analytics_controller.get_total_answers_per_question(question_id, db)

@router.get("/users/{user_id}/answer-history")
def user_history(user_id: int, db: Session = Depends(get_db)):
    return analytics_controller.get_user_answer_history(user_id, db)

@router.get("/users/{user_id}/total-answered")
def user_total(user_id: int, db: Session = Depends(get_db)):
    return analytics_controller.get_total_questions_answered_by_user(user_id, db)

@router.get("/summary")
def system_summary(db: Session = Depends(get_db)):
    return analytics_controller.get_full_system_summary(db)
