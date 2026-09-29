from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from uuid import uuid4
import random

from database import get_db
from models import Transaction, Card
from schemas import PaymentRequest, PaymentResponse
from auth import get_current_user


router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@router.post("/", response_model=PaymentResponse)
def make_payment(
    payment: PaymentRequest,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    # Check that the card exists and belongs to the logged-in user
    card = db.query(Card).filter(
        Card.id == payment.card_id,
        Card.user_id == current_user_id
    ).first()

    if not card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card not found or does not belong to the current user"
        )

    transaction_reference = f"TXN-{uuid4().hex[:12].upper()}"

    transaction = Transaction(
        user_id=current_user_id,
        card_id=payment.card_id,
        amount=payment.amount,
        status="PENDING",
        transaction_reference=transaction_reference,
        created_at=func.now()
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    # Simulate payment processing
    payment_success = random.choice([True, False])

    if payment_success:
        transaction.status = "SUCCESS"
    else:
        transaction.status = "FAILED"

    db.commit()
    db.refresh(transaction)

    return PaymentResponse(
        transaction_id=transaction.id,
        transaction_reference=transaction.transaction_reference,
        amount=transaction.amount,
        status=transaction.status
    )