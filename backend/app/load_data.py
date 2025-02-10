import redis

# Conexão com Redis
redis_client = redis.StrictRedis(host="localhost", port=6379, decode_responses=True)

# Criar um quiz
redis_client.hset("quiz:1", mapping={
    "title": "Quiz de Geografia",
    "creator": "Prof. João",
    "duration": 20
})

# Criar perguntas
redis_client.hset("question:101", mapping={
    "quiz_id": "1",
    "question": "Qual a capital da França?",
    "A": "Paris",
    "B": "Londres",
    "C": "Berlim",
    "D": "Madri",
    "correct_answer": "A"
})

redis_client.hset("question:102", mapping={
    "quiz_id": "1",
    "question": "Qual o maior oceano do mundo?",
    "A": "Atlântico",
    "B": "Índico",
    "C": "Pacífico",
    "D": "Ártico",
    "correct_answer": "C"
})

# Inserir votos simulados
redis_client.hincrby("votes:101", "A", 50)
redis_client.hincrby("votes:101", "B", 10)
redis_client.hincrby("votes:101", "C", 20)
redis_client.hincrby("votes:101", "D", 5)

redis_client.hincrby("votes:102", "A", 30)
redis_client.hincrby("votes:102", "B", 5)
redis_client.hincrby("votes:102", "C", 60)
redis_client.hincrby("votes:102", "D", 2)

# Simular tempos de resposta
redis_client.rpush("response_time:101", 10, 15, 20, 12)
redis_client.rpush("response_time:102", 8, 14, 18, 9)

# Ranking de alunos (pontuação)
redis_client.zadd("ranking:scores", {"aluno_1": 50, "aluno_2": 40, "aluno_3": 70})

print("Dados carregados no Redis!")
