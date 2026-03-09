from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Dict, Optional


MODEL_VERSION = os.getenv('MODEL_VERSION', 'baseline_xgboost_v1')
T_MID = float(os.getenv('T_MID', '0.10'))
T_HIGH = float(os.getenv('T_HIGH', '0.30'))

MODEL_DIR = Path(__file__).resolve().parents[1] / 'models'
METADATA_PATH = MODEL_DIR / 'metadata.json'
XGB_JSON_PATH = MODEL_DIR / 'xgboost_model.json'


def load_metadata() -> Dict:
    if METADATA_PATH.exists():
        return json.loads(METADATA_PATH.read_text(encoding='utf-8'))
    return {
        'note': 'No trained XGBoost artifact found. Using heuristic fallback scorer.',
        'features': [
            'step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest',
            'deltaOrig', 'deltaDest', 'isOrigBalanceZero', 'isDestBalanceZero', 'isFlaggedFraud', 'type'
        ]
    }


def _sigmoid(x: float) -> float:
    import math
    return 1.0 / (1.0 + math.exp(-x))


def _to_numeric_features(features: Dict) -> Dict[str, float]:
    tx_type = str(features.get('type', 'PAYMENT'))
    return {
        'step': float(features.get('step', 0)),
        'amount': float(features.get('amount', 0)),
        'oldbalanceOrg': float(features.get('oldbalanceOrg', 0)),
        'newbalanceOrig': float(features.get('newbalanceOrig', 0)),
        'oldbalanceDest': float(features.get('oldbalanceDest', 0)),
        'newbalanceDest': float(features.get('newbalanceDest', 0)),
        'deltaOrig': float(features.get('deltaOrig', 0)),
        'deltaDest': float(features.get('deltaDest', 0)),
        'isOrigBalanceZero': float(features.get('isOrigBalanceZero', 0)),
        'isDestBalanceZero': float(features.get('isDestBalanceZero', 0)),
        'isFlaggedFraud': float(features.get('isFlaggedFraud', 0)),
        'type_CASH_IN': 1.0 if tx_type == 'CASH_IN' else 0.0,
        'type_CASH_OUT': 1.0 if tx_type == 'CASH_OUT' else 0.0,
        'type_DEBIT': 1.0 if tx_type == 'DEBIT' else 0.0,
        'type_PAYMENT': 1.0 if tx_type == 'PAYMENT' else 0.0,
        'type_TRANSFER': 1.0 if tx_type == 'TRANSFER' else 0.0,
    }


def fallback_score(features: Dict) -> float:
    """
    XGBoost artifact 不存在時的保底 scorer。
    """
    amount = float(features.get('amount', 0.0))
    delta_orig = float(features.get('deltaOrig', 0.0))
    delta_dest = float(features.get('deltaDest', 0.0))
    flagged = int(features.get('isFlaggedFraud', 0))
    tx_type = str(features.get('type', ''))

    z = -6.2
    z += 0.000003 * amount
    z += 0.000002 * max(delta_orig, 0.0)
    z += 0.000002 * max(delta_dest, 0.0)
    z += 2.2 * flagged
    if tx_type in {'TRANSFER', 'CASH_OUT'}:
        z += 0.7

    return max(0.0, min(1.0, _sigmoid(z)))


class XGBScorer:
    def __init__(self) -> None:
        self.booster: Optional[object] = None
        self.feature_names: list[str] = []
        self.enabled = False

        try:
            import xgboost as xgb  # type: ignore
            if XGB_JSON_PATH.exists():
                booster = xgb.Booster()
                booster.load_model(str(XGB_JSON_PATH))
                self.booster = booster
                self.feature_names = list(booster.feature_names or [])
                self.enabled = True
        except Exception:
            self.enabled = False

    def score(self, features: Dict) -> float:
        if not self.enabled or self.booster is None:
            return fallback_score(features)

        import pandas as pd
        import xgboost as xgb  # type: ignore

        row = _to_numeric_features(features)
        cols = self.feature_names if self.feature_names else list(row.keys())
        X = pd.DataFrame([{c: row.get(c, 0.0) for c in cols}], columns=cols)
        dmat = xgb.DMatrix(X, feature_names=cols)
        pred = float(self.booster.predict(dmat)[0])
        return max(0.0, min(1.0, pred))


SCORER = XGBScorer()


def score(features: Dict) -> float:
    return SCORER.score(features)


def risk_level(prob: float) -> str:
    if prob >= T_HIGH:
        return 'HIGH'
    if prob >= T_MID:
        return 'MEDIUM'
    return 'LOW'
