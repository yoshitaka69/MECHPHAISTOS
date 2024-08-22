from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, GanttTestListView  # GanttTestListViewをインポート

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('gantt-tests/', GanttTestListView.as_view(), name='gantt-test-list'),  # 新しいルートを追加
]