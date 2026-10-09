from fastapi import FastAPI
from app.database import Base, engine, get_db
from app.routers import PerguntaRouter

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GeoAssist AI",
    description="API de um assistente inteligente para análise de ocorrências geográficas.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(PerguntaRouter.router)