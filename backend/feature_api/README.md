# Feature API

A FastAPI-based service for transforming transaction data into model-ready features.

## Getting Started

### Prerequisites

- [uv](https://docs.astral.sh/uv/) (recommended) or Python 3.12+

### Local Development

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Run the development server**:
   ```bash
   uv run fastapi dev
   ```
   The API will be available at `http://127.0.0.1:8000`.

3. **Explore documentation**:
   Visit `http://127.0.0.1:8000/docs` for interactive API documentation.

### Run with Docker

1. **Build the image**:
   ```bash
   docker build -t feature-api .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8080:8080 feature-api
   ```

## API Endpoints

- `GET /health`: Health check endpoint.
- `POST /v1/features/transform`: Transform a single transaction.
- `POST /v1/features/transform-batch`: Transform multiple transactions.
