from pydantic import BaseModel, Field
from decimal import Decimal


class PaymentRequest(BaseModel):
    card_id: int
    amount: Decimal = Field(gt=0)


class PaymentResponse(BaseModel):
    transaction_id: int
    transaction_reference: str
    amount: Decimal
    status: str