# Multi-stage build to keep the production image clean and small
FROM python:3.11-slim AS builder

WORKDIR /app

# Create a virtual environment for dependency isolation
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy and install only production dependencies first (to leverage Docker build cache)
COPY requirements/base.txt ./requirements/base.txt
RUN pip install --no-cache-dir -r ./requirements/base.txt

# Final runtime stage
FROM python:3.11-slim AS runner

WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application code
COPY ./app ./app
COPY ./scripts ./scripts

# Ensure run scripts are executable
RUN chmod +x ./scripts/*.sh

# Expose the API port
EXPOSE 8000

# Run the application in production mode using Gunicorn with Uvicorn workers
CMD ["gunicorn", "app.main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
