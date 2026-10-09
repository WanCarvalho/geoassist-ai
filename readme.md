# GeoAssist AI

Assistente inteligente para análise de ocorrências geográficas, desenvolvido como projeto de estudo e portfólio para praticar a construção de uma aplicação fullstack com frontend Angular, API Python/FastAPI, persistência em banco de dados e futura integração com inteligência artificial generativa.

> **Status:** em desenvolvimento. Até o momento, a API inicial está implementada e os três testes automatizados existentes passam. A resposta da aplicação ainda é simulada; a integração real com um serviço de IA será implementada em uma etapa futura.

## Objetivos do projeto

- Construir uma API REST com FastAPI e Python.
- Validar dados de entrada e estruturar respostas com Pydantic.
- Persistir perguntas e respostas usando SQLAlchemy.
- Criar testes automatizados com `pytest` e `TestClient`.
- Desenvolver futuramente uma interface Angular para interação com o assistente.
- Integrar futuramente um serviço de IA por meio do backend, mantendo credenciais fora do frontend.
- Evoluir a organização do código, a configuração do banco, a documentação e a execução do projeto.

## Tecnologias utilizadas

| Tecnologia | Uso atual ou planejado |
|---|---|
| Python 3.11 | Linguagem do backend |
| FastAPI | Construção da API REST |
| Pydantic | Validação dos dados de entrada e definição das respostas |
| SQLAlchemy | Mapeamento objeto-relacional (ORM) e acesso ao banco |
| SQLite | Banco de dados local usado atualmente |
| pytest | Execução dos testes automatizados |
| HTTPX / TestClient | Testes dos endpoints HTTP |
| Angular | Frontend planejado |
| PostgreSQL | Alternativa planejada para uma etapa futura |
| Docker / Docker Compose | Containerização planejada |
| API de IA generativa | Integração planejada |

## Funcionalidades implementadas

### Verificação de saúde da API

**`GET /health`**

Verifica se a aplicação está respondendo.

Resposta atual:

```json
{
  "status": "ok"
}
```

### Criar pergunta

**`POST /api/perguntas`**

Recebe uma pergunta, valida o conteúdo, registra a pergunta e uma resposta simulada no banco de dados e devolve o registro criado.

Exemplo de requisição:

```json
{
  "pergunta": "O que é atividade sísmica?"
}
```

A resposta é simulada neste estágio e segue o formato:

```text
Resposta simulada para: O que é atividade sísmica?
```

O schema valida a pergunta para que tenha entre 1 e 2.000 caracteres. Uma pergunta vazia é rejeitada pela validação da API.

### Listar perguntas

**`GET /api/perguntas`**

Retorna as perguntas registradas, ordenadas pelo identificador em ordem decrescente.

### Documentação interativa

O FastAPI disponibiliza a documentação Swagger UI em `/docs`, permitindo consultar e executar os endpoints pelo navegador enquanto a aplicação está em execução.

## Estrutura atual do backend

```text
geoassist-ai/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── tests/
│   │   └── test_perguntas.py
│   ├── .venv/
│   ├── requirements.txt
│   └── geoassist.db          # criado localmente durante a execução
└── frontend/                 # reservado para a aplicação Angular
```

A pasta `.venv/` e o arquivo `geoassist.db` são artefatos locais de execução e não devem ser tratados como código-fonte do projeto.

### Responsabilidade dos arquivos

- **`app/main.py`** — cria a aplicação FastAPI e declara as rotas HTTP.
- **`app/database.py`** — configura a conexão SQLite, o engine SQLAlchemy, a fábrica de sessões e a dependência `get_db`, que fornece uma sessão aos endpoints e a fecha ao final do uso.
- **`app/models.py`** — define o modelo ORM `Pergunta` e a tabela `perguntas`, com os campos `id`, `pergunta`, `resposta` e `criada_em`.
- **`app/schemas.py`** — define os schemas Pydantic de entrada e saída, incluindo a validação do tamanho da pergunta.
- **`tests/test_perguntas.py`** — contém os testes automatizados dos endpoints básicos.
- **`requirements.txt`** — registra as dependências Python do projeto.

## Configuração e execução local

### Pré-requisitos

- Python 3.11 ou compatível.
- PowerShell no Windows (os comandos abaixo usam esse terminal).

### 1. Acessar o backend

Na raiz do projeto:

```powershell
cd backend
```

### 2. Criar e ativar o ambiente virtual

Caso o ambiente ainda não exista:

```powershell
python -m venv .venv
```

Ative-o no PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação por política de execução, ajuste a configuração de acordo com as políticas da sua máquina; não é necessário alterar políticas globais sem necessidade.

### 3. Instalar dependências

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

> Se o arquivo `requirements.txt` ainda não estiver atualizado com todas as dependências instaladas no ambiente, gere-o conforme a seção abaixo.

### 4. Iniciar a API

Execute a partir da pasta `backend`:

```powershell
uvicorn app.main:app --reload
```

Endereços locais:

- API: `http://127.0.0.1:8000`
- Documentação Swagger: `http://127.0.0.1:8000/docs`
- Verificação de saúde: `http://127.0.0.1:8000/health`

Para interromper o servidor, use `Ctrl+C` no terminal.

## Dependências Python

As principais dependências instaladas durante a configuração inicial foram:

- `fastapi[standard]`
- `sqlalchemy`
- `alembic`
- `psycopg[binary]`
- `pytest`
- `httpx`

Para atualizar `requirements.txt` com as versões instaladas no ambiente virtual ativo, execute na pasta `backend`:

```powershell
python -m pip freeze > requirements.txt
```

Esse comando registra todas as distribuições instaladas no ambiente, incluindo dependências transitivas. Para manter o arquivo enxuto no futuro, podemos separar dependências diretas das dependências de desenvolvimento.

## Modelo de dados atual

A tabela `perguntas` contém:

| Campo | Finalidade |
|---|---|
| `id` | Identificador primário do registro |
| `pergunta` | Texto enviado pelo usuário |
| `resposta` | Resposta gerada pela lógica atual, ainda simulada |
| `criada_em` | Data e hora de criação, preenchida por padrão em UTC |

Atualmente, o banco está configurado como SQLite por meio da URL `sqlite:///./geoassist.db`. O arquivo é criado no diretório de trabalho usado para iniciar a aplicação.

O código utiliza `Base.metadata.create_all()` para criar as tabelas definidas pelos modelos quando a aplicação é inicializada. A adoção de migrações com Alembic será importante para evoluir o schema de forma controlada.

## Testes automatizados

Execute os testes a partir da pasta `backend`:

```powershell
python -m pytest tests/test_perguntas.py -v
```

### Testes existentes

| Teste | O que verifica |
|---|---|
| `test_health_check` | O endpoint `/health` retorna HTTP 200 e `{"status": "ok"}` |
| `test_criar_pergunta` | A criação retorna HTTP 200 e inclui pergunta, resposta, identificador e data de criação |
| `test_rejeitar_pergunta_vazia` | O envio de uma pergunta vazia retorna HTTP 422 |

**Último resultado registrado:** `3 passed`. Foi exibido um aviso de depreciação relacionado à integração entre `starlette.testclient` e `httpx`; ele não impediu a execução dos testes.

> **Limitação conhecida:** os testes ainda utilizam a configuração de banco da aplicação. Isolar os testes com um banco separado e temporário é uma das próximas tarefas, para evitar que os testes alterem os dados locais de desenvolvimento.

## Conceitos praticados até aqui

- **Modelos ORM e schemas não são a mesma coisa:** o modelo SQLAlchemy representa os dados persistidos; os schemas Pydantic validam e estruturam os dados recebidos e devolvidos pela API.
- **`db.add()`** adiciona um objeto à sessão para persistência.
- **`db.commit()`** confirma a transação no banco; não fecha a sessão.
- **`db.refresh()`** recarrega os atributos do objeto a partir do banco, por exemplo, para obter valores gerados durante a persistência.
- **`Depends(get_db)`** permite que o FastAPI forneça a sessão ao endpoint sem repetir a lógica de abertura e encerramento em cada rota.
- **`yield` em `get_db()`** permite executar a limpeza e fechar a sessão ao final do uso da dependência.
- **Testes automatizados** verificam comportamentos esperados e ajudam a detectar regressões durante a evolução do projeto.

## Próximas etapas planejadas

- [ ] Isolar os testes usando um banco de dados de teste independente.
- [ ] Adicionar testes para listagem e outros casos de validação.
- [ ] Revisar a configuração e a organização das dependências Python.
- [ ] Definir configurações por ambiente e retirar valores de configuração do código.
- [ ] Integrar uma API real de IA pelo backend, tratando erros e tempos de espera.
- [ ] Criar a interface Angular para enviar perguntas e exibir respostas.
- [ ] Melhorar a persistência e avaliar a migração para PostgreSQL.
- [ ] Gerenciar alterações de schema com Alembic.
- [ ] Adicionar Docker e Docker Compose.
- [ ] Ampliar a documentação e os testes de integração.

As etapas podem mudar conforme os requisitos e o aprendizado durante o desenvolvimento.

## Segurança e configuração

- Não coloque chaves de API de IA no código-fonte nem no frontend.
- Não envie arquivos `.env`, credenciais, ambientes virtuais ou dados locais do banco para o repositório.
- Quando as integrações externas forem adicionadas, carregue as credenciais por variáveis de ambiente e documente as variáveis necessárias em um arquivo de exemplo sem valores secretos.
- Antes de publicar o projeto, revise o `.gitignore` para excluir arquivos locais e informações sensíveis.

## Status do projeto

O backend possui uma estrutura inicial organizada, três endpoints/comportamentos básicos cobertos pelos testes e persistência local com SQLite. A resposta de IA ainda é simulada; frontend Angular, banco de testes isolado, integração real com IA, PostgreSQL e Docker permanecem como evoluções futuras.
