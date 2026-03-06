from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.answer import Answer
from app.models.question import Question

def get_option_counts_per_question(question_id: int, db: Session):
    results = (
        db.query(Answer.selected_option, func.count(Answer.id).label("count"))
        .filter(Answer.question_id == question_id)
        .group_by(Answer.selected_option)
        .all()
    )
    counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    for option, count in results:
        counts[option] = count
    return {"question_id": question_id, "option_counts": counts}

def get_total_answers_per_question(question_id: int, db: Session):
    total = db.query(func.count(Answer.id)).filter(Answer.question_id == question_id).scalar()
    return {"question_id": question_id, "total_answers": total}

def get_user_answer_history(user_id: int, db: Session):
    answers = db.query(Answer).filter(Answer.user_id == user_id).all()
    return {
        "user_id": user_id,
        "total_answered": len(answers),
        "answers": [
            {"question_id": a.question_id, "selected_option": a.selected_option,
             "answered_at": a.created_at, "updated_at": a.updated_at}
            for a in answers
        ]
    }

def get_total_questions_answered_by_user(user_id: int, db: Session):
    total = db.query(func.count(Answer.id)).filter(Answer.user_id == user_id).scalar()
    return {"user_id": user_id, "total_questions_answered": total}

def get_full_system_summary(db: Session):
    total_questions = db.query(func.count(Question.id)).scalar()
    total_answers = db.query(func.count(Answer.id)).scalar()
    unique_users = db.query(func.count(func.distinct(Answer.user_id))).scalar()
    per_question = (
        db.query(Answer.question_id, func.count(Answer.id).label("answer_count"))
        .group_by(Answer.question_id).all()
    )
    return {
        "total_questions": total_questions,
        "total_answers": total_answers,
        "unique_users_who_answered": unique_users,
        "answers_per_question": [{"question_id": qid, "answer_count": c} for qid, c in per_question]
    }
