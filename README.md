# FastAPI Calculator

A FastAPI application that evaluates mathematical expressions safely using Python's built-in AST (Abstract Syntax Tree) parser — no `eval()`, no external math libraries.

## Project Structure

```text
fastapi-calculator/
├── app/                        # Main application code
│   ├── __init__.py
│   ├── main.py                 # FastAPI application instance and initialization
│   │
│   ├── api/                    # API routing and endpoints
│   │   ├── __init__.py
│   │   ├── dependencies/       # Reusable FastAPI dependencies
│   │   └── v1/                 # API Version 1
│   │       ├── __init__.py
│   │       ├── api.py          # Aggregates all v1 routers
│   │       └── endpoints/      # Individual endpoint modules
│   │           ├── __init__.py
│   │           └── calculator.py
│   │
│   ├── core/                   # Application-wide configurations
│   │   └── config.py           # Environment variables (Pydantic BaseSettings)
│   │
│   ├── schemas/                # Pydantic models (request & response validation)
│   │   ├── __init__.py
│   │   └── calculator.py
│   │
│   └── services/               # Core business logic
│       ├── __init__.py
│       └── calculator.py       # AST-based expression evaluator
│
├── tests/                      # Automated tests (pytest)
│   ├── conftest.py             # Shared fixtures (TestClient)
│   ├── api/
│   │   └── test_endpoints.py   # Integration tests for the API layer
│   └── services/
│       └── test_logic.py       # Unit tests for the service layer
│
├── requirements/               # Python dependencies
│   ├── base.txt                # Production dependencies
│   └── dev.txt                 # Development dependencies (includes pytest, black)
│
├── scripts/                    # Execution scripts
│   ├── run_dev.sh              # Local development server (uvicorn --reload)
│   └── run_prod.sh             # Production server (Gunicorn + Uvicorn workers)
│
├── .env.example                # Template for environment variables
├── .gitignore                  # Git ignore file
├── Makefile                    # Developer command aliases
└── README.md                   # Project documentation
```

## Getting Started

### 1. Setup the Virtual Environment
Create a virtual environment and install all dependencies (requires Python 3.11+):
```bash
make install
```

### 2. Make scripts executable (Mac/Linux only)
```bash
chmod +x scripts/run_dev.sh scripts/run_prod.sh
```

### 3. Run the Test Suite
```bash
make tests
```

### 4. Run the Development Server
```bash
make run-dev
```

### 5. Run the Production Server
```bash
make run-prod
```

The API will be available at [http://localhost:8000](http://localhost:8000).  
Check out the interactive API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

## API Usage

### `POST /api/v1/calculator/`

Evaluates a mathematical expression and returns the result.

**Request body:**
```json
{
  "expression": "10 * (3 + 2) / 5"
}
```

**Response:**
```json
{
  "result": 10.0
}
```

**Supported operators:** `+`, `-`, `*`, `/`, unary `-` and `+`, and parentheses `()`.

**Error response (400):** Returned for invalid or unsupported expressions.
```json
{
  "detail": "Division by zero is not allowed"
}
```

**Error response (422):** Returned by Pydantic when the request body is malformed (e.g., missing `expression` field or empty string).

## Developer Commands

| Command | Description |
|---|---|
| `make install` | Create venv and install all dependencies |
| `make tests` | Run the full test suite with pytest |
| `make format` | Auto-format code with Black |
| `make run-dev` | Start the uvicorn development server (auto-reload) |
| `make run-prod` | Start the Gunicorn production server (4 workers) |
