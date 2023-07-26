
from utils.django_setup import django_setup
import logging
from fastapi import FastAPI, status
from django.conf import settings
from starlette.middleware import Middleware
# from fast.middleware.device_id import DeviceIDMiddlewares
from fastapi.middleware.cors import CORSMiddleware
from starlette_context.middleware import RawContextMiddleware
# from fast.middleware.device_id import DeviceIDMiddleware
# from fast.middleware.utms import UTMsMiddleware


def get_application() -> FastAPI:
    django_setup()

    # middlewares = [
    #     Middleware(RawContextMiddleware),
    #     Middleware(DeviceIDMiddleware),
    #     Middleware(UTMsMiddleware),
    # ]

    app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG, middleware=[])

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    from .routers import orders,home, tracks
    app.include_router(home.router)
    app.include_router(orders.router, prefix='/orders')
    app.include_router(tracks.router, prefix='/tracks')

    return app

app = get_application()

logging.info('Ready for API requests')