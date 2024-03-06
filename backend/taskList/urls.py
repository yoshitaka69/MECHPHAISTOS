from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet,company_task_list,TaskByCompanyViewSet

router = DefaultRouter()
router.register(r'task', TaskViewSet, basename='task')

urlpatterns = [
    path('task/', include(router.urls)),
    path('company-task/', company_task_list, name='company-task'),
    path('task-by-company/<str:companyCode_slug>/', TaskByCompanyViewSet.as_view({'get': 'list'}), name='task-by-company')
]