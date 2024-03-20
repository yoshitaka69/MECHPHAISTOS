from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskListViewSet,CompanyCodeTaskListViewSet

router = DefaultRouter()
router.register(r'taskList', TaskListViewSet, basename='taskList')
router.register(r'taskListByCompany', CompanyCodeTaskListViewSet, basename='companyCode-taskList')

urlpatterns = [
    path('task/', include(router.urls)),
]