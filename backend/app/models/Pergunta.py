from datetime import datetime, timezone
from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Pergunta(Base):
    __tablename__ = "perguntas"
    
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )
    pergunta: Mapped[str] = mapped_column(
        Text, nullable=False
    )
    resposta: Mapped[str] = mapped_column(
        Text, nullable=False
    )
    criada_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )