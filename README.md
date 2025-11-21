# Carreira em TI – Scanner de Afinidades (100 perguntas, tema futurista)

App **FastAPI + HTML/JS** com **fluxo de 1 pergunta por vez** (auto-avança ao selecionar) e **tema futurista**.  
Perguntas **sem jargão técnico** (assumimos zero conhecimento prévio).  
Resultado com **ranking de áreas** (Programação, Infra, Segurança, Dados, Design, Games), **arquétipos** e **export JSON**.

## Rodar localmente

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install fastapi uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8090
```
Abra: http://localhost:8090

## Docker

```bash
docker build -t carreira-ti-100-futuristic .
docker run --rm -p 8090:8090 carreira-ti-100-futuristic
```
Acesse: http://localhost:8090

## Endpoints

- `GET /` – UI (fluxo 1-a-1)
- `GET /api/questions` – perguntas + metadados
- `POST /api/score` – recebe `[{id, value}]` e retorna ranking normalizado
- `GET /healthz` – health check

## Observações

- A escala é 1 (Nenhum Interesse) a 5 (Muito Interessado).
- As perguntas não citam ferramentas (sem Ansible, Terraform, Kubernetes, etc.).
- Mapeamento invisível no backend relaciona cada pergunta a uma **área** e **perfil**.
