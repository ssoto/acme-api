from pydantic import BaseModel, Field
from typing import Optional

class Character(BaseModel):
    """Modelo para representar un personaje de ACME"""
    name: str = Field(..., min_length=2, max_length=50, description="Nombre del personaje")
    age: int = Field(..., gt=0, lt=150, description="Edad del personaje")
    description: str = Field(..., min_length=10, max_length=500, description="Descripción del personaje")
    greeting: str = Field(..., min_length=5, max_length=100, description="Saludo característico del personaje")

    def is_adult(self) -> bool:
        """Verifica si el personaje es adulto"""
        return self.age >= 18
