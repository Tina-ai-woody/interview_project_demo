# Model API

A FastAPI-based service for predicting fraud risk using pre-trained machine learning models.

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
   The API will be available at `http://127.0.0.1:8001` (Note: default dev port might vary, check terminal output).

3. **Explore documentation**:
   Visit `http://127.0.0.1:8001/docs` for interactive API documentation.

### Run with Docker

1. **Build the image**:
   ```bash
   docker build -t model-api .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8081:8081 model-api
   ```

## API Endpoints

- `GET /health`: Health check and model metadata endpoint.
- `POST /v1/model/predict`: Predict risk for a single transaction.
- `POST /v1/model/predict-batch`: Predict risk for multiple transactions.
