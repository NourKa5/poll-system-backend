from fastapi import FastAPI
from app.db.database import engine, Base
from app.routes.user_routes import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Service", description="Manages users and registration status", version="1.0.0")
app.include_router(user_router)

@app.get("/health")
def health_check():
    return {"status": "User Service is running"}
