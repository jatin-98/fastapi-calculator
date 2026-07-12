# FastAPI Calculator

An industry-standard FastAPI application designed for learning Python and modern web API architecture.

## Project Structure

This project follows a highly scalable, enterprise-grade directory structure:

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
│   │   ├── __init__.py
│   │   ├── config.py           # Environment variables (Pydantic BaseSettings)
│   │   └── exceptions.py       # Custom exception handlers
│   │
│   ├── schemas/                # Pydantic models (Data validation)
│   │   ├── __init__.py
│   │   └── calculator.py       
│   │
│   └── services/               # Core business logic
│       ├── __init__.py
│       └── calculator.py       
│
├── tests/                      # Automated tests (pytest)
│   ├── api/                    
│   └── services/               
│
├── requirements/               # Python dependencies
│   ├── base.txt                # Production dependencies
│   └── dev.txt                 # Development dependencies
│
├── scripts/                    # Execution scripts
│   ├── run_dev.sh              # Local development server
│   └── run_prod.sh             # Production server (Gunicorn)
│
├── .env.example                # Template for environment variables
├── .gitignore                  # Git ignore file
├── docker-compose.yml          # Local environment orchestration
├── Dockerfile                  # Production image definition
├── Makefile                    # Developer aliases
└── README.md                   # Project documentation
```

## Getting Started

### 1. Setup the Virtual Environment
Create a virtual environment and install the required dependencies (requires Python 3.11+):
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

## Development Phases

Once the basic routing is set up, development of the calculator functionality should proceed in three distinct phases:

### Phase 1: Define the Data (The Schemas)
Create `app/schemas/calculator.py` using Pydantic to validate incoming JSON requests (e.g., ensuring a `CalculatorRequest` receives a valid mathematical `expression` string).

### Phase 2: Build the Brains (The Services)
Create `app/services/calculator.py`. Write pure Python math functions (like an AST parser) here. This keeps business logic completely separate from FastAPI endpoints.

### Phase 3: Connect the Endpoint
Update `app/api/v1/endpoints/calculator.py` to receive the validated data (from Phase 1), pass it to the math functions (from Phase 2), and return the final result to the user.
