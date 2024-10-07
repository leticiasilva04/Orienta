"""
ASGI config for projeto_orienta project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from chat import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_orienta.settings')

application = get_asgi_application()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '<nome_do_seu_projeto>.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                path('ws/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),  # WebSocket URL
            ]
        )
    ),
})
