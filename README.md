# Carreira em TI – Questionário (100 perguntas, sem jargões) – Porta 8090

App **FastAPI + HTML/JS** que aplica um questionário **Likert (1–5)** com **100 perguntas** (sem termos técnicos) e recomenda **áreas de TI** (Programação, Infraestrutura, Segurança, Dados, Design, Games) e um **perfil/arquétipo** (Analista, Construtor, Inovador, Comunicador). Inclui **exportação do resultado em JSON**.

## Rodando localmente (sem Docker)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install fastapi uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8090
```

Abra: http://localhost:8090

## Docker

```bash
docker build -t carreira-ti-100-agnostico-8090 .
docker run --rm -p 8090:8090 carreira-ti-100-agnostico-8090
```

Acesse: http://localhost:8090

## Coolify

- **Internal Port / Ports Exposes**: `8090`
- **Ports Mappings**: deixe **vazio** (o proxy do Coolify cuida do 80/443) ou use `8090:8090`.
- **Domain**: apenas o host (ex.: `teste.inteligencia.it`, sem `http://`).
- Após o deploy, o Coolify emite o certificado TLS automaticamente.

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
- O resultado de cada categoria = **soma** das respostas (1..5).
- O backend **normaliza em % (0–100)** com base na quantidade de perguntas por categoria.
- A resposta inclui **Top 3 Áreas**, **Ranking Completo** e **Perfil dominante**.
- O frontend gera um **arquivo JSON** com toda a resposta do backend para você baixar.
