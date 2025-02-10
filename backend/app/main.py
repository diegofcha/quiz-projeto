from fastapi import FastAPI
from app.routes import quizzes, votes, ranking  
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Quiz API", version="1.0")

# Importando as rotas
app.include_router(quizzes.router)
app.include_router(votes.router)
app.include_router(ranking.router)

@app.get("/")
def home():
    return {"message": "API de Quiz Gamificado está rodando!"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)