# Carreira em TI – Scanner de Afinidades (100 perguntas, tema futurista, **mobile-first**)

- Fluxo 1 pergunta por vez, **avança automaticamente** ao selecionar.
- **Totalmente mobile-friendly**: botões grandes, grade adaptativa (1/2/3/5 colunas), sticky progress e safe-area.
- Perguntas **sem jargão técnico**.
- Resultado com ranking de áreas, perfis e **download JSON**.

## Rodar localmente
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install fastapi uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8090
```
Abra: http://localhost:8090

## Docker
```bash
docker build -t carreira-ti-100-futuristic-mobile .
docker run --rm -p 8090:8090 carreira-ti-100-futuristic-mobile
```
Acesse: http://localhost:8090

## Coolify
- **Build Pack**: Dockerfile
- **Internal Port (Ports Exposes)**: 8090
- **Ports Mappings**: vazio (ou 8090:8090)
- **Domains**: `teste.inteligencia.it` (sem http/https)
