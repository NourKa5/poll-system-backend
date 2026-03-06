from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.question import Question
from app.schemas.question import QuestionCreate, QuestionUpdate

def get_all_questions(db: Session):
    return db.query(Question).all()

def get_question_by_id(question_id: int, db: Session):
    q = db.query(Question).filter(Question.id == question_id).first()
    if not q:
        raise HTTPException(status_code=404, detail=f"Question {question_id} not found")
    return q

def create_question(data: QuestionCreate, db: Session):
    question = Question(**data.model_dump())
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

def update_question(question_id: int, data: QuestionUpdate, db: Session):
    question = get_question_by_id(question_id, db)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(question, key, value)
    db.commit()
    db.refresh(question)
    return question

def delete_question(question_id: int, db: Session):
    question = get_question_by_id(question_id, db)
    db.delete(question)
    db.commit()
    return {"message": f"Question {question_id} deleted successfully"}
