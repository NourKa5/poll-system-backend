from fastapi import FastAPI
from app.db.database import engine, Base
from app.routes.question_routes import router as question_router
from app.routes.answer_routes import router as answer_router
from app.routes.analytics_routes import router as analytics_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Poll Service", description="Manages questions, answers, and analytics", version="1.0.0")
app.include_router(question_router)
app.include_router(answer_router)
app.include_router(analytics_router)

@app.get("/health")
def health_check():
    return {"status": "Poll Service is running"}
