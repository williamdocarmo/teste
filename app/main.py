from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, conint
from typing import List, Dict, Any
from .questions import QUESTIONS, DOMAIN_LABELS_PT, PERSONA_LABELS_PT

app = FastAPI(title="Carreira TI - Questionário (100 perguntas)")

# Servir arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/api/questions")
def get_questions():
    """
    Retorna a lista de perguntas com seus metadados (id, texto, domínio, arquétipo).
    """
    return {"questions": QUESTIONS, "domains": DOMAIN_LABELS_PT, "personas": PERSONA_LABELS_PT}


class Answer(BaseModel):
    id: int = Field(..., description="ID da pergunta")
    value: conint(ge=1, le=5) = Field(..., description="Resposta Likert 1..5")


class ScoreResponse(BaseModel):
    domain_scores: Dict[str, Any]
    persona_scores: Dict[str, Any]
    domain_ranking: List[Dict[str, Any]]
    persona_ranking: List[Dict[str, Any]]
    summary: Dict[str, Any]


@app.post("/api/score", response_model=ScoreResponse)
def score(answers: List[Answer]):
    # Índice rápido por id
    q_by_id = {q["id"]: q for q in QUESTIONS}

    # Inicializa acumuladores
    domains = {key: 0 for key in DOMAIN_LABELS_PT.keys()}
    personas = {key: 0 for key in PERSONA_LABELS_PT.keys()}
    counts_domain = {key: 0 for key in DOMAIN_LABELS_PT.keys()}
    counts_persona = {key: 0 for key in PERSONA_LABELS_PT.keys()}

    # Pré-contagem de itens por categoria (para normalização)
    for q in QUESTIONS:
        counts_domain[q["domain"]] += 1
        counts_persona[q["persona"]] += 1

    # Soma das respostas
    for a in answers:
        q = q_by_id.get(a.id)
        if not q:
            continue
        domains[q["domain"]] += a.value
        personas[q["persona"]] += a.value

    # Normalização (0..100)
    def normalize(raw: Dict[str, int], counts: Dict[str, int]) -> Dict[str, float]:
        norm = {}
        for k, v in raw.items():
            max_possible = counts[k] * 5 if counts[k] > 0 else 1
            norm[k] = round((v / max_possible) * 100.0, 2)
        return norm

    domain_norm = normalize(domains, counts_domain)
    persona_norm = normalize(personas, counts_persona)

    # Rankings
    domain_ranking = sorted(
        [{"key": k, "label": DOMAIN_LABELS_PT[k], "score": domain_norm[k], "raw": domains[k], "questions": counts_domain[k]} for k in domain_norm],
        key=lambda x: x["score"],
        reverse=True
    )

    persona_ranking = sorted(
        [{"key": k, "label": PERSONA_LABELS_PT[k], "score": persona_norm[k], "raw": personas[k], "questions": counts_persona[k]} for k in persona_norm],
        key=lambda x: x["score"],
        reverse=True
    )

    summary = {
        "top_domains": domain_ranking[:3],
        "top_persona": persona_ranking[0] if persona_ranking else None,
        "interpretation": {
            "hint": "Use os percentuais como direção: acima de 70% indica forte afinidade; 50–70% afinidade moderada; abaixo de 50% indica tema a explorar com calma."
        }
    }

    return ScoreResponse(
        domain_scores=domain_norm,
        persona_scores=persona_norm,
        domain_ranking=domain_ranking,
        persona_ranking=persona_ranking,
        summary=summary
    )


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    with open("app/static/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())