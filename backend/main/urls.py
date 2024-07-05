from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import os

# 環境変数で無効にするアプリケーションを指定
disabled_apps = os.getenv('DISABLE_APPS', '').split(',')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include('djoser.urls')),
    path("api/", include('djoser.urls.authtoken')),
    path("api/", include('accounts.urls')),
    path("api/", include('ceList.urls')),
    path("api/", include('nearMiss.urls')),
    path("api/", include('sustainability.urls')),
    path("api/", include('repairingCost.urls')),
    path("api/", include('spareParts.urls')),
    path("api/", include('taskList.urls')),
    path("api/", include('junctionTable.urls')),
    path("api/", include('calculation.urls')),
    path("api/", include('agora.urls')),
    path("api/", include('workOrder.urls')),
    path("api/", include('reliability.urls')),
    path("api/", include('workingReport.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'audio_recognition' not in disabled_apps:
    urlpatterns.append(path('minutes/', include('audio_recognition.urls')))

if 'ai' not in disabled_apps:
    urlpatterns.append(path('api/', include('ai.urls')))

if 'scada' not in disabled_apps:
    urlpatterns.append(path('scada/', include('scada.urls')))

if 'channels' not in disabled_apps:
    # channels関連のURLパターンを追加
    pass
