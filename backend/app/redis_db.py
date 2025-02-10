import redis

# Conexão com Redis (rodando localmente no Docker)
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
