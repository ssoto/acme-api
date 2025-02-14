from src.models import Character

def test_character_creation(single_character):
    """Test para verificar la creación correcta de un personaje"""
    assert single_character.name == "Bugs Bunny"
    assert single_character.age == 35
    assert "conejo astuto" in single_character.description
    assert single_character.greeting == "¿Qué hay de nuevo, viejo?"

def test_characters_list(sample_characters):
    """Test para verificar la lista de personajes"""
    assert len(sample_characters) == 10
    assert all(isinstance(char, Character) for char in sample_characters)
    assert any(char.name == "Wile E. Coyote" for char in sample_characters)

def test_is_adult_with_adult_character():
    """Test para verificar que un personaje mayor de 18 años es considerado adulto"""
    adult_character = Character(
        name="Elmer Fudd",
        age=50,
        description="Un cazador torpe que siempre persigue a Bugs Bunny",
        greeting="Shhh... estoy cazando conejos"
    )
    assert adult_character.is_adult() is True

def test_is_adult_with_minor_character():
    """Test para verificar que un personaje menor de 18 años no es considerado adulto"""
    minor_character = Character(
        name="Tweety",
        age=15,
        description="Un pequeño canario amarillo que siempre evade a Silvestre",
        greeting="¡Me pareció ver un lindo gatito!"
    )
    assert minor_character.is_adult() is False

def test_is_adult_with_exactly_eighteen():
    """Test para verificar que un personaje de exactamente 18 años es considerado adulto"""
    character = Character(
        name="Test Character",
        age=18,
        description="Un personaje de prueba que tiene exactamente 18 años",
        greeting="¡Hola Mundo!"
    )
    assert character.is_adult() is True


