
from utils.django_setup import django_setup
import logging
from fastapi import FastAPI, status
from django.conf import settings



def get_application() -> FastAPI:
    django_setup()

    app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)

    from .routers import orders,home
    app.include_router(home.router, prefix='/home')
    app.include_router(orders.router, prefix='/order')

    return app

app = get_application()

logging.info('Ready for API requests')