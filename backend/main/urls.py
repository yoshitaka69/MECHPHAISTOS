from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include




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
    path('', include('audio_recognition.urls')),
    path('api/', include('ai.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
