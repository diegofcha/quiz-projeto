# 🎯 Projeto Quiz - FastAPI & Next.js 🚀

Este projeto é um sistema gamificado de Quiz para cursos online com milhares de alunos acessando simultaneamente.

## 📌 Tecnologias Utilizadas
- 🐍 **Backend:** FastAPI + Redis
- 🌐 **Frontend:** Next.js (React)
- 🗄️ **Banco de Dados:** Redis
- 🐳 **Containerização:** Docker

## ⚙️ Como Rodar o Projeto

### 1️⃣ Clone o Repositório
```bash
git clone https://github.com/diegofcha/quiz-projeto.git
cd quiz-projeto
```
---

### 🚀 **2️⃣ Configurar e Rodar o Backend**
1. Vá para a pasta do backend:
```bash
cd backend
```
2. Ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Rodar FastAPI:
```bash
uvicorn app.main:app --reload
```
🔗 Swagger: http://127.0.0.1:8000/docs
🔗 Redoc: http://127.0.0.1:8000/redoc

### 🚀 **3️⃣ Configurar e Rodar o Frontend**
1. Vá para a pasta do backend:
```bash
cd ../quiz-frontend
```
2. Instale as dependências:
```bash
npm install
```
3. Rodar servidor:
```bash
npm run dev
```
🔗 http://localhost:3000


