# Carreira em TI – Questionário (100 perguntas) com Export JSON

App **FastAPI + HTML/JS** que aplica um questionário **Likert (1–5)** com **100 perguntas** e recomenda **áreas de TI** (Programação, Infraestrutura, Segurança, Dados, Design, Games) e um **perfil/arquétipo** (Analista, Construtor, Inovador, Comunicador).

Agora com **botão para baixar um JSON** com o resultado completo (percentuais, rankings e resumo).

## Rodando localmente (sem Docker)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install fastapi uvicorn
uvicorn app.main:app --reload
```

Abra: http://localhost:8000

## Docker

```bash
docker build -t carreira-ti-100-json .
docker run --rm -p 8000:8000 carreira-ti-100-json
```

Acesse: http://localhost:8000

## Endpoints

- `GET /` – UI (HTML)
- `GET /api/questions` – perguntas + metadados
- `POST /api/score` – recebe `[{id, value}]` e retorna ranking normalizado
- `GET /healthz` – health check

## Escala

1 = Nenhum Interesse  
2 = Pouco Interesse  
3 = Moderado  
4 = Interessado  
5 = Muito Interessado

## Como funciona a “inteligência”

- Cada pergunta pertence a **uma área** e a **um arquétipo**.
- O resultado de cada categoria = **soma** das respostas 1..5.
- O backend **normaliza em % (0–100)** com base na **quantidade de perguntas** por categoria.
- A resposta inclui **Top 3 Áreas**, **Ranking Completo** e **Perfil dominante**.
- O frontend gera um **arquivo JSON** com toda a resposta do backend para você baixar.
