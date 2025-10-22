"""
ASGI config for FastAPI Project.

It exposes the ASGI callable as a module-level variable named ``application``.

"""

# import os
from app.main import app


# os.environ.setdefault('some_env', 'django_project.settings')

application = app