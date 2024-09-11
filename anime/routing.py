from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/watch_together/(?P<room_name>\w+)/$', consumers.WatchTogetherConsumer.as_asgi()),
    re_path('ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi())
]
