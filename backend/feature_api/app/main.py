import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .schemas import (
    TransactionInput,
    FeatureOutput,
    BatchTransactionInput,
    BatchFeatureOutput,
)
from .transformers import transform_single


app = FastAPI(title='feature-api', version='0.1.0')

allowed_origins = os.getenv(
    'ALLOWED_ORIGINS',
    'http://localhost:3000,http://127.0.0.1:3000'
).split(',')

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in allowed_origins if origin.strip()],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/health')
def health():
    return {'status': 'ok', 'service': 'feature-api'}


@app.post('/v1/features/transform', response_model=FeatureOutput)
def transform(payload: TransactionInput):
    return transform_single(payload)


@app.post('/v1/features/transform-batch', response_model=BatchFeatureOutput)
def transform_batch(payload: BatchTransactionInput):
    return BatchFeatureOutput(items=[transform_single(x) for x in payload.items])
