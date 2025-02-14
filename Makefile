.PHONY: test coverage run install

# Variables
PYTHON = python
PORT = 8000
HOST = 0.0.0.0
VENV = .venv
VENV_BIN = $(VENV)/bin
UV = $(shell which uv)

# Instalación del proyecto y dependencias
install:
	@echo "Verificando/Instalando uv..."
	@command -v uv >/dev/null 2>&1 || curl -LsSf https://astral.sh/uv/install.sh | sh
	@echo "Creando entorno virtual..."
	@$(UV) venv $(VENV)
	@echo "Instalando dependencias..."
	@. $(VENV)/bin/activate && $(UV) pip install -e ".[test]"
	@echo "Instalación completada ✨"

# Ejecutar los tests
test:
	$(VENV_BIN)/pytest

# Generar reporte de cobertura
coverage:
	$(VENV_BIN)/pytest --cov=src --cov-report=html
	@echo "El reporte de cobertura está disponible en htmlcov/index.html"

# Ejecutar el servidor de desarrollo
run:
	$(VENV_BIN)/uvicorn src.main:app --host $(HOST) --port $(PORT) --reload

# Ayuda
help:
	@echo "Comandos disponibles:"
	@echo "  make install    - Instalar dependencias del proyecto"
	@echo "  make test       - Ejecutar tests"
	@echo "  make coverage   - Generar reporte de cobertura"
	@echo "  make run       - Iniciar servidor de desarrollo" 