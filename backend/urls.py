from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls), #adminサイト
    path('api/', include('ce.API.urls')), #API表示

    #re_path(r"^.*$", IndexView.as_view()),#これは一番最後に置く　admin/とapi/v1/以外のパスをIndexViewでキャッチ
]