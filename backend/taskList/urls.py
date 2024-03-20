from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskListPM02ViewSet,CompanyCodeTaskListPM02ViewSet,TaskListPM03ViewSet,CompanyCodeTaskListPM03ViewSet,TaskListPM04ViewSet,CompanyCodeTaskListPM04ViewSet,TaskListPM05ViewSet,CompanyCodeTaskListPM05ViewSet



router = DefaultRouter()
router.register(r'taskListPM02', TaskListPM02ViewSet, basename='taskListPM02')
router.register(r'taskListPM02ByCompany', CompanyCodeTaskListPM02ViewSet, basename='companyCode-taskListPM02')
router.register(r'taskListPM03', TaskListPM03ViewSet, basename='taskListPM03')
router.register(r'taskListPM03ByCompany', CompanyCodeTaskListPM03ViewSet, basename='companyCode-taskListPM03')
router.register(r'taskListPM04', TaskListPM04ViewSet, basename='taskListPM04')
router.register(r'taskListPM04ByCompany', CompanyCodeTaskListPM04ViewSet, basename='companyCode-taskListPM04')
router.register(r'taskListPM05', TaskListPM05ViewSet, basename='taskListPM05')
router.register(r'taskListPM05ByCompany', CompanyCodeTaskListPM05ViewSet, basename='companyCode-taskListPM05')

urlpatterns = [
    path('task/', include(router.urls)),
]