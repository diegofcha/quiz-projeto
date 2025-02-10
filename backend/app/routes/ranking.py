from fastapi import APIRouter
from app.redis_db import redis_client

router = APIRouter(prefix="/ranking", tags=["Ranking"])

@router.get("/alternativas-mais-votadas/{question_id}")
def get_top_alternatives(question_id: str):
    vote_key = f"votes:{question_id}"
    votes = redis_client.hgetall(vote_key)
    return {"alternativas": sorted(votes.items(), key=lambda x: int(x[1]), reverse=True)}

@router.get("/questoes-mais-acertadas/")
def get_top_questions():
    top_questions = redis_client.zrevrange("ranking:acertos", 0, 9, withscores=True)
    return {"questoes_mais_acertadas": [{"question_id": q[0], "acertos": int(q[1])} for q in top_questions]}

@router.get("/questoes-com-mais-abstencoes/")
def get_most_abstained_questions():
    top_questions = redis_client.zrevrange("ranking:abstencoes", 0, 9, withscores=True)
    return {"questoes_com_mais_abstencoes": [{"question_id": q[0], "abstencoes": int(q[1])} for q in top_questions]}

@router.get("/tempo-medio/{question_id}")
def get_average_response_time(question_id: str):
    response_key = f"response_time:{question_id}"
    times = redis_client.lrange(response_key, 0, -1)
    avg_time = sum(map(float, times)) / len(times) if times else 0
    return {"question_id": question_id, "tempo_medio": avg_time}

@router.get("/alunos-com-maior-acerto/")
def get_top_students():
    top_students = redis_client.zrevrange("ranking:acertos", 0, 9, withscores=True)
    return {"alunos_mais_acertos": [{"user_id": s[0], "acertos": int(s[1])} for s in top_students]}

@router.get("/alunos-mais-rapidos/")
def get_fastest_students():
    fastest_students = redis_client.zrange("ranking:tempo", 0, 9, withscores=True)
    return {"alunos_mais_rapidos": [{"user_id": s[0], "tempo_medio": float(s[1])} for s in fastest_students]}

@router.get("/rank-final/")
def get_final_ranking():
    final_ranking = redis_client.zrevrange("ranking:final", 0, 9, withscores=True)
    return {"rank_final": [{"user_id": s[0], "pontuacao_final": float(s[1])} for s in final_ranking]}
