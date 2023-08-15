from fastapi import FastAPI

from .routers import customer, user, authentication

app = FastAPI()

app.include_router(authentication.router)

app.include_router(customer.router)

app.include_router(user.router)

