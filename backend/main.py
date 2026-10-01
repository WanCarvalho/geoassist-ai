from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="GeoAssist AI",
    description="API de um assistente inteligente para análise de ocorrências geográficas.",
    version="0.1.0",
)


class PerguntaRequest(BaseModel):
    pergunta: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/api/perguntas")
def criar_pergunta(dados: PerguntaRequest):
    return {
        "pergunta": dados.pergunta,
        "resposta": f"Pergunta recebida: {dados.pergunta}",
    }