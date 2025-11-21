# Carreira em TI – Scanner (Futurista / Mobile-first)

- 100 perguntas sem jargão técnico
- Fluxo **1 por vez** com **auto-avançar**
- **Tema futurista** e **CSS mobile-first**
- Exporta **JSON** do resultado
- Porta **8090**

## Docker
```bash
docker build -t carreira-ti-100-futuristic-mobile .
docker run --rm -p 8090:8090 carreira-ti-100-futuristic-mobile
# http://localhost:8090
```

## Coolify
- Build Pack: Dockerfile
- Internal Port / Ports Exposes: `8090`
- Ports Mappings: vazio (ou `8090:8090`)
- Domain: `teste.inteligencia.it`
