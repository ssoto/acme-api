import pytest
from src.models import Character

@pytest.fixture
def sample_characters():
    """Fixture que genera una lista de 10 personajes de ejemplo"""
    characters = [
        Character(
            name="Wile E. Coyote",
            age=45,
            description="Un coyote superinteligente obsesionado con atrapar al Correcaminos",
            greeting="¡Esta vez sí lo atraparé!"
        ),
        Character(
            name="Road Runner",
            age=30,
            description="Un veloz correcaminos que siempre escapa de Wile E. Coyote",
            greeting="¡Beep beep!"
        ),
        Character(
            name="Bugs Bunny",
            age=35,
            description="Un conejo astuto y carismático que siempre se sale con la suya",
            greeting="¿Qué hay de nuevo, viejo?"
        ),
        Character(
            name="Daffy Duck",
            age=40,
            description="Un pato egocéntrico y competitivo que siempre acaba en problemas",
            greeting="¡Eres despreciable!"
        ),
        Character(
            name="Elmer Fudd",
            age=50,
            description="Un cazador torpe que siempre persigue a Bugs Bunny",
            greeting="Shhh... estoy cazando conejos"
        ),
        Character(
            name="Porky Pig",
            age=35,
            description="Un cerdito tartamudo pero adorable que siempre es optimista",
            greeting="¡Eso... eso... eso es todo amigos!"
        ),
        Character(
            name="Tweety",
            age=15,
            description="Un pequeño canario amarillo que siempre evade a Silvestre",
            greeting="¡Me pareció ver un lindo gatito!"
        ),
        Character(
            name="Sylvester",
            age=40,
            description="Un gato persistente que siempre intenta atrapar a Tweety",
            greeting="¡Por las barbas de Neptuno!"
        ),
        Character(
            name="Taz",
            age=30,
            description="Un demonio de Tasmania que se convierte en un tornado al girar",
            greeting="¡Blblblblblbl!"
        ),
        Character(
            name="Marvin the Martian",
            age=149,
            description="Un marciano decidido a destruir la Tierra porque le bloquea la vista de Venus",
            greeting="Esto me hace muy feliz, muy feliz de verdad"
        )
    ]
    return characters

@pytest.fixture
def single_character():
    """Fixture que devuelve un único personaje de ejemplo"""
    return Character(
        name="Bugs Bunny",
        age=35,
        description="Un conejo astuto y carismático que siempre se sale con la suya",
        greeting="¿Qué hay de nuevo, viejo?"
    ) 