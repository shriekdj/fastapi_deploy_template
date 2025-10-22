"""
WSGI config for FastAPI Project.

It exposes the WSGI callable as a module-level variable named ``application``.

"""

# import os
from app.main import app
from a2wsgi import ASGIMiddleware


# os.environ.setdefault('some_env', 'django_project.settings')

application = ASGIMiddleware(app)