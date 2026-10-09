from fastapi import APIRouter, Depends, HTTPException, status
from app.models.Pergunta import Pergunta
from app.database import get_db
from app.schemas.PerguntaSchema import PerguntaResponse, PerguntaCreate
from sqlalchemy.orm import Session
from datetime import datetime, timezone

router = APIRouter(prefix="/api/perguntas", tags=["perguntas"])


@router.post("/", response_model=PerguntaResponse)
async def criar_pergunta(
    dados: PerguntaCreate,
    db: Session = Depends(get_db)
):
    pergunta = Pergunta(
        pergunta=dados.pergunta,
        resposta=f"Resposta simulada para: {dados.pergunta}"
    )
    
    db.add(pergunta)
    db.commit()
    db.refresh(pergunta)
    
    return pergunta


@router.get("/", response_model=list[PerguntaResponse])
async def listar_perguntas(db: Session = Depends(get_db)):
    return (
        db.query(Pergunta)
        .order_by(Pergunta.id.desc())
        .all()
    )