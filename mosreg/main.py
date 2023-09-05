from fastapi import FastAPI

from mosreg.routers import archive_payment, commentment

from .routers import payment, user, authentication
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"]
)

app.include_router(authentication.router)

app.include_router(payment.router)

app.include_router(archive_payment.router)

app.include_router(commentment.router)

app.include_router(user.router)

