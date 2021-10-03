from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import Chat_Room.routing
application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            Chat_Room.routing.websocket_urlpatterns
        )
    ),
})