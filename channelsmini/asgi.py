# """
# ASGI config for channelsmini project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
# """

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channelsmini.settings')

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import livechat.routing
from django.core.asgi import get_asgi_application
# # from channels.http import AsgiHandler
# # from channels.routing import ProtocolTypeRouter



application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            livechat.routing.websocket_urlpatterns
        )
    ),
})
# # import django

# # django.setup()

# # application = ProtocolTypeRouter({
# #   "http": AsgiHandler(),
# #   # Just HTTP for now. (We can add other protocols later.)
# # })