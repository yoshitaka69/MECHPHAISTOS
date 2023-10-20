from django.contrib import admin
from django.urls import path, include, re_path
from ce.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls), #adminサイト
    path('api/v1/', include('ce.urls')), #API表示
    path('ce/', include('ce.urls')), #重要機器リスト表示

    #re_path(r"^.*$", IndexView.as_view()),#これは一番最後に置く　admin/とapi/v1/以外のパスをIndexViewでキャッチ
]