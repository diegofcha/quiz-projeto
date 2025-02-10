from fastapi import APIRouter
from pydantic import BaseModel
from app.redis_db import redis_client

router = APIRouter(prefix="/votes", tags=["Votos"])

class VoteRequest(BaseModel):
    quiz_id: str
    question_id: str
    option: str
    user_id: str
    response_time: float  # Tempo que o aluno levou para responder

@router.post("/")
def vote(vote_data: VoteRequest):
    valid_options = ["A", "B", "C", "D"]

    if vote_data.option not in valid_options:
        return {"error": "Opção inválida! Escolha entre A, B, C ou D"}

    vote_key = f"votes:{vote_data.question_id}"
    redis_client.hincrby(vote_key, vote_data.option, 1)  # Salva o voto no Redis

    # Armazena tempo de resposta na lista do Redis
    response_key = f"response_time:{vote_data.question_id}"
    redis_client.rpush(response_key, vote_data.response_time)

    # Atualizar ranking de alunos por acertos (se resposta estiver correta)
    correct_answer = redis_client.hget(f"question:{vote_data.question_id}", "correct_answer")
    if correct_answer == vote_data.option:
        redis_client.zincrby("ranking:acertos", 1, vote_data.user_id)

    # Atualizar ranking de tempo de resposta dos alunos
    redis_client.zadd("ranking:tempo", {vote_data.user_id: vote_data.response_time})

    # Atualizar ranking final (baseado em acertos e tempo de resposta)
    score = redis_client.zscore("ranking:acertos", vote_data.user_id) or 0
    final_score = score - (vote_data.response_time / 10)  # Penaliza tempo maior
    redis_client.zadd("ranking:final", {vote_data.user_id: final_score})

    return {"message": f"Voto para {vote_data.option} computado com sucesso!"}


@router.get("/{quiz_id}")
def get_votes(quiz_id: str):
    vote_key = f"votes:{quiz_id}"
    votes = redis_client.hgetall(vote_key)
    return {"votes": votes}
