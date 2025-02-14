from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .models import Character
from .infrastructure import CharactersDB

# Crear la instancia de FastAPI
app = FastAPI(
    title="ACME API",
    description="API REST con FastAPI para ACME",
    version="0.1.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Instanciar la base de datos
characters_db = CharactersDB()

@app.get("/")
async def root():
    """Endpoint raíz que devuelve un mensaje de bienvenida"""
    return {
        "message": "¡Bienvenido a la API de ACME!",
        "docs": "/docs",
        "status": "active"
    }

@app.get("/health")
async def health_check():
    """Endpoint para verificar el estado de la API"""
    return {
        "status": "healthy",
        "version": app.version
    }

@app.get("/characters", response_model=List[Character], tags=["characters"])
async def get_characters():
    """
    Obtiene la lista completa de personajes ACME
    """
    return characters_db.get_all()

@app.get("/characters/search", response_model=List[Character], tags=["characters"])
async def search_characters(
    query: str = Query(..., min_length=3, description="Palabra o frase a buscar en la descripción")
):
    """
    Busca personajes que contengan la palabra o frase especificada en su descripción
    """
    return characters_db.search_by_description(query)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 