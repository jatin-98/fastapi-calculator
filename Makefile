.PHONY: install run-dev run-prod tests format

# ANSI Color Codes
GREEN = \033[0;32m
BLUE = \033[0;34m
NC = \033[0m # No Color

install:
	@printf "${BLUE}==> Creating virtual environment and installing dependencies...${NC}\n"
	python3.11 -m venv venv
	./venv/bin/pip install -r requirements/dev.txt
	@printf "${GREEN}==> Installation complete!${NC}\n"

run-dev:
	@printf "${BLUE}==> Starting FastAPI Development Server...${NC}\n"
	./scripts/run_dev.sh

run-prod:
	@printf "${BLUE}==> Starting Gunicorn Production Server...${NC}\n"
	./scripts/run_prod.sh

tests:
	@printf "${BLUE}==> Running Pytest...${NC}\n"
	./venv/bin/pytest tests/ -v

format:
	@printf "${BLUE}==> Formatting code with Black...${NC}\n"
	./venv/bin/black app/ tests/
	@printf "${GREEN}==> Code formatting complete!${NC}\n"