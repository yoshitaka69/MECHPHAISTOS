from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskListViewSet,company_task_list,TaskListByCompanyViewSet

router = DefaultRouter()
router.register(r'task', TaskListViewSet, basename='task')

urlpatterns = [
    path('task/', include(router.urls)),
    path('company-task/', company_task_list, name='company-task'),
    path('task-by-company/<str:companyCode_slug>/', TaskListByCompanyViewSet.as_view({'get': 'list'}), name='task-by-company')
]