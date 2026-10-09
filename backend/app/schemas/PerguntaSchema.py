from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class PerguntaCreate(BaseModel):
    pergunta: str = Field(min_length=1, max_length=2000)
    
    
class PerguntaResponse(BaseModel):
    id: int
    pergunta: str
    resposta: str
    criada_em: datetime
    
    model_config = ConfigDict(from_attributes=True)