from fastapi import APIRouter
from app.redis_db import redis_client

router = APIRouter(prefix="/quizzes", tags=["Quizzes"])

@router.get("/")
def get_all_quizzes():
    quiz_keys = redis_client.keys("quiz:*")
    quizzes = []

    for key in quiz_keys:
        quiz_data = redis_client.hgetall(key)
        quiz_data["quiz_id"] = key.split(":")[-1]  # Corrigido para remover .decode()
        
        # Converte options de string para lista, caso necessário
        if isinstance(quiz_data.get("options"), str):
            quiz_data["options"] = quiz_data["options"].split(",")

        quizzes.append(quiz_data)

    return {"quizzes": quizzes}
