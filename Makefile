# Makefile for FastAPI project with Alembic migrations

# Variables
PYTHON=python3.9
POETRY=poetry
ALEMBIC=$(POETRY) run alembic
APP_MODULE=main:app  # Update with the path to your FastAPI app
HOST=127.0.0.1
PORT=8000

.PHONY: help install run dev migrate upgrade downgrade alembic-init create-migration

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## Install project dependencies
	$(POETRY) install

run: ## Run the FastAPI application
	$(POETRY) run uvicorn $(APP_MODULE) --host $(HOST) --port $(PORT)

dev: ## Run the FastAPI application in development mode (with auto-reload)
	$(POETRY) run uvicorn $(APP_MODULE) --host $(HOST) --port $(PORT) --reload

migrate: ## Run Alembic migrations (upgrade to the latest version)
	$(ALEMBIC) upgrade head

upgrade: ## Upgrade to a specific Alembic revision
	$(ALEMBIC) upgrade $(REVISION)

downgrade: ## Downgrade to a specific Alembic revision
	$(ALEMBIC) downgrade $(REVISION)

alembic-init: ## Initialize Alembic in the project
	$(POETRY) run alembic init alembic

create-migration: ## Create a new Alembic migration
	@read -p "Enter migration message: " MESSAGE; \
	$(ALEMBIC) revision --autogenerate -m "$$MESSAGE"