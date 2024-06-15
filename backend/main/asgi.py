
#DjangoはデフォルトでWSGI (Web Server Gateway Interface) を使用していますが、リアルタイム通信やWebSocketのような非同期機能をサポートするためにASGIが必要です。ASGIは非同期処理をサポートしており、チャットアプリケーションやリアルタイムデータフィードなどに適しています。



import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import audio_recognition.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            audio_recognition.routing.websocket_urlpatterns
        )
    ),
})
