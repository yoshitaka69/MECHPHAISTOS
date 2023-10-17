from django.contrib import admin
from django.urls import path, include, re_path
from ce.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('ce.urls')),
    re_path(r"^.*$", IndexView.as_view()),
]