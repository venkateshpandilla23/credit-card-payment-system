from fastapi import FastAPI

from routes.payments import router as payment_router


app = FastAPI(
    title="Credit Card Payment System API",
    description="FastAPI backend for payment processing",
    version="1.0.0"
)


app.include_router(payment_router)


@app.get("/")
def home():
    return {
        "message": "Credit Card Payment System FastAPI is running"
    }