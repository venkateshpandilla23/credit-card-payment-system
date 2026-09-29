import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_payment_requires_authentication():
    response = client.post(
        "/payments/",
        json={
            "card_id": 2,
            "amount": 500
        }
    )

    assert response.status_code == 401


def test_payment_rejects_invalid_token():
    response = client.post(
        "/payments/",
        headers={
            "Authorization": "Bearer invalid-token"
        },
        json={
            "card_id": 2,
            "amount": 500
        }
    )

    assert response.status_code == 401


def test_payment_rejects_zero_amount_without_auth():
    response = client.post(
        "/payments/",
        json={
            "card_id": 2,
            "amount": 0
        }
    )

    assert response.status_code == 401