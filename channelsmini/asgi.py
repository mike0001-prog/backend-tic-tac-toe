# """
# ASGI config for channelsmini project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
# """

# import os
# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channelsmini.settings')

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# import livechat.routing
# # # from channels.http import AsgiHandler
# # # from channels.routing import ProtocolTypeRouter



# application = ProtocolTypeRouter({
#   "http": get_asgi_application(),
#   "websocket": AuthMiddlewareStack(
#         URLRouter(
#             livechat.routing.websocket_urlpatterns
#         )
#     ),
# })
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channelsmini.settings')

from django.core.asgi import get_asgi_application

# ✅ Initialize Django first
django_asgi_app = get_asgi_application()

# ✅ Now it's safe to import Channels stuff
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import livechat.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
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