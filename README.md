# Poll System Backend

**Student:** Nour Karawani
**Course:** AI Developer  
**Tech Stack:** FastAPI · MySQL · Docker · Docker Compose

---

## Project Overview

A Poll System Backend built as two fully independent microservices, each running in its own Docker container with its own MySQL database.

---

## Services

### User Service (Port 8001)
Manages users and registration status.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/users/` | Get all users |
| GET | `/users/{id}` | Get user by ID |
| GET | `/users/email/{email}` | Get user by email |
| POST | `/users/` | Create a user |
| PUT | `/users/{id}` | Update a user |
| DELETE | `/users/{id}` | Delete a user |
| GET | `/users/{id}/registration-status` | Check if user is registered |

### Poll Service (Port 8002)
Manages questions, answers, and analytics.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/questions/` | Get all questions |
| GET | `/questions/{id}` | Get question by ID |
| POST | `/questions/` | Create a question |
| PUT | `/questions/{id}` | Update a question |
| DELETE | `/questions/{id}` | Delete a question |
| GET | `/answers/` | Get all answers |
| POST | `/answers/` | Submit an answer |
| PUT | `/answers/user/{user_id}/question/{question_id}` | Update an answer |
| DELETE | `/answers/{id}` | Delete an answer |
| GET | `/analytics/questions/{id}/option-counts` | Option counts per question |
| GET | `/analytics/questions/{id}/total-answers` | Total answers per question |
| GET | `/analytics/users/{id}/answer-history` | User answer history |
| GET | `/analytics/users/{id}/total-answered` | Total questions answered by user |
| GET | `/analytics/summary` | Full system summary |

---

## How to Run

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop)

### Start the project
```bash
docker-compose up --build
```

### Access the APIs
- User Service: http://localhost:8001/docs
- Poll Service: http://localhost:8002/docs

### Stop the project
```bash
docker-compose down
```

---

## Project Structure

```
poll_system/
├── docker-compose.yml
├── user_service/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── db/database.py
│       ├── models/user.py
│       ├── schemas/user.py
│       ├── controllers/user_controller.py
│       └── routes/user_routes.py
└── poll_service/
    ├── Dockerfile
    ├── requirements.txt
    └── app/
        ├── main.py
        ├── db/database.py
        ├── models/question.py
        ├── models/answer.py
        ├── schemas/question.py
        ├── schemas/answer.py
        ├── controllers/question_controller.py
        ├── controllers/answer_controller.py
        ├── controllers/analytics_controller.py
        ├── routes/question_routes.py
        ├── routes/answer_routes.py
        └── routes/analytics_routes.py
```

---

## Key Rules
- Only **registered users** can submit answers
- Each user can only submit **one answer per question**
- Answers can be **updated** but not duplicated
- Deleting a question automatically deletes all its answers
