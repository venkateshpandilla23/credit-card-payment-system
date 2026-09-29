# Credit Card Payment System

A backend-focused Credit Card Payment System built using Django, FastAPI, MySQL, and Docker.

## Technologies Used

- Python
- Django
- Django REST Framework
- FastAPI
- MySQL
- JWT Authentication
- SQLAlchemy
- Docker
- Docker Compose
- Postman
- Swagger / OpenAPI
- Git and GitHub

## Project Structure

```text
credit-card-payment-system/
│
├── backend/
│   ├── django_backend/
│   │   ├── config/
│   │   ├── users/
│   │   ├── cards/
│   │   ├── transactions/
│   │   ├── admin_panel/
│   │   ├── templates/
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── manage.py
│   │
│   └── fastapi_backend/
│       ├── routes/
│       ├── tests/
│       ├── auth.py
│       ├── database.py
│       ├── models.py
│       ├── schemas.py
│       ├── main.py
│       ├── Dockerfile
│       └── requirements.txt
│
├── database/
├── postman/
├── screenshots/
├── docker-compose.yml
├── .gitignore
└── README.md