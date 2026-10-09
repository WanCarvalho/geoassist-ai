from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    
    
def test_criar_pergunta():
    response = client.post(
        "/api/perguntas",
        json={"pergunta": "O que é atividade sísmica?"}
    )
    
    assert response.status_code == 200
    
    data = response.json()
    assert data["pergunta"] == "O que é atividade sísmica?"
    assert data["resposta"] == "Resposta simulada para: O que é atividade sísmica?"
    assert "id" in data
    assert "criada_em" in data
    
    
def test_rejeitar_pergunta_vazia():
    response = client.post(
        "/api/perguntas",
        json={"pergunta": ""}
    )
    
    assert response.status_code == 422