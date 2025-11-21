# Carreira em TI – Scanner (150 perguntas, tema futurista, mobile-first)

- **150 perguntas** (25 por área), sem jargões, focadas em preferências cognitivas/comportamentais.
- **Fluxo 1 a 1**: escolheu → avança sozinho. **Swipe para voltar** e botões touch grandes.
- **Sem segmento na pergunta** (apenas "Pergunta X/150").
- **Toast + destaque** para perguntas não respondidas.
- **Export JSON** dos resultados.
- **Porta 8090** no container.

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
docker build -t carreira-ti-150-futuristic-mobile .
docker run --rm -p 8090:8090 carreira-ti-150-futuristic-mobile
```
Acesse: http://localhost:8090

## Coolify
- Build Pack: **Dockerfile**
- Internal Port (Ports Exposes): **8090**
- Ports Mappings: vazio (ou 8090:8090)
- Domains: `teste.inteligencia.it` (sem http/https)

## Dica
Use `?compact=1` na URL para opções “1·2·3·4·5” em vez de rótulos longos.
