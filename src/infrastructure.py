from typing import List, Optional
from .models import Character

class CharactersDB:
    """Clase que gestiona el almacenamiento y operaciones de los personajes"""
    
    def __init__(self):
        """Inicializa la base de datos con algunos personajes por defecto"""
        self._characters: List[Character] = [
            Character(
                name="Wile E. Coyote",
                age=45,
                description="Un coyote superinteligente obsesionado con atrapar al Correcaminos",
                greeting="¡Esta vez sí lo atraparé!"
            ),
            Character(
                name="Bugs Bunny",
                age=35,
                description="Un conejo astuto y travieso",
                greeting="¿Qué hay de nuevo, viejo?"
            ), 
            Character(
                name="El Correcaminos",
                age=30,
                description="Un corredor rápido y travieso",
                greeting="¡Vamos a ver quién es el más rápido!"
            ),
        ]

    def get_all(self) -> List[Character]:
        """Obtiene todos los personajes"""
        return self._characters

    def add(self, character: Character) -> Character:
        """Añade un nuevo personaje"""
        self._characters.append(character)
        return character

    def search_by_description(self, query: str) -> List[Character]:
        """Busca personajes por descripción"""
        query = query.lower()
        return [
            character for character in self._characters 
            if query in character.description.lower()
        ]

    def get_by_name(self, name: str) -> Optional[Character]:
        """Obtiene un personaje por su nombre"""
        for character in self._characters:
            if character.name.lower() == name.lower():
                return character
        return None

    def clear(self):
        """Limpia la base de datos - útil para testing"""
        self._characters.clear()

    def bulk_add(self, characters: List[Character]):
        """Añade múltiples personajes de una vez - útil para testing"""
        self._characters.extend(characters) 