from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.app.config import settings
from src.api.v1.api import api_router
from src.api.v1.endpoints import auth, cities, points, enrichment

app = FastAPI(
    title=f"{settings.PROJECT_NAME} — API REST",
    version=settings.VERSION,
    description="""
    API RESTful e Sistema Web para Consulta e Inserção de Pontos de Vacinação no Estado de Alagoas.
    Trabalho Acadêmico do Projeto Integrador IV - B (PostgreSQL 16, FastAPI, Jinja2, Tailwind e Docker).
    """,
    docs_url="/docs",
    redoc_url="/redoc"
)

# RNF-03: CORS habilitado
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# RNF-04: Tratamento Global de Erros Internos
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Erro interno no servidor. Contate os desenvolvedores do projeto."}
    )

# 1. Rotas Diretas na Raiz (Exigência Estrita dos Slides da Disciplina: /cities e /vaccination-points)
app.include_router(cities.router, prefix="/cities", tags=["Municípios (cities)"])
app.include_router(points.router, prefix="/vaccination-points", tags=["Pontos de Vacinação (vaccination-points)"])
app.include_router(points.router, prefix="/admin/vaccination-points", tags=["Pontos de Vacinação (Admin Alias)"], include_in_schema=False)
app.include_router(auth.router, prefix="/auth", tags=["Autenticação Administrativa"])
app.include_router(enrichment.router, prefix="/admin/enrichment", tags=["Bot de Enriquecimento (OSM)"])

# 2. Rotas Versionadas (/api/v1/...)
app.include_router(api_router, prefix=settings.API_V1_STR)
