from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, GanttTestListView  # GanttTestListViewをインポート
from .views import get_tree_data

# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)

router.register(r'products', ProductViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('gantt-tests/', GanttTestListView.as_view(), name='gantt-test-list'),  # 新しいルートを追加
     path('tree-data/', get_tree_data, name='tree-data'),
]