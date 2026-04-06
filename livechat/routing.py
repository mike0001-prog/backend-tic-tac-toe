from django.urls import re_path,path

from . import consumer

websocket_urlpatterns = [
    # re_path(r'ws/live/(?P<room_name>\w+)/$', consumer.Chat.as_asgi()),
    re_path(r'ws/online/(?P<room_name>\w+)/$',consumer.Game.as_asgi())
]