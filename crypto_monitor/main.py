import os
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

app = FastAPI()
app.mount("/admin", WSGIMiddleware(get_asgi_application()))

from routes import router
app.include_router(router)

