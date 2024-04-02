from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (TaskListPPM02ViewSet,CompanyCodeTaskListPPM02ViewSet,
                    TaskListAPM02ViewSet,CompanyCodeTaskListAPM02ViewSet,

                    TaskListPPM03ViewSet,CompanyCodeTaskListPPM03ViewSet,
                    TaskListAPM03ViewSet,CompanyCodeTaskListAPM03ViewSet,

                    TaskListAPM04ViewSet,CompanyCodeTaskListAPM04ViewSet,

                    TaskListPPM05ViewSet,CompanyCodeTaskListPPM05ViewSet,
                    TaskListAPM05ViewSet,CompanyCodeTaskListAPM05ViewSet,

                    TypicalTaskListViewSet,CompanyCodeTypicalTaskListViewSet,
                    TaskListViewSet,CompanyCodeTaskListViewSet)



router = DefaultRouter()
router.register(r'typicalTaskList', TypicalTaskListViewSet, basename='typicalTaskList')
router.register(r'typicalTaskListByCompany', CompanyCodeTypicalTaskListViewSet, basename='companyCode-typicalTaskList')

router.register(r'taskList', TaskListViewSet, basename='taskList')
router.register(r'taskListByCompany', CompanyCodeTaskListViewSet, basename='companyCode-taskList')

router.register(r'taskListPPM02', TaskListPPM02ViewSet, basename='taskListPPM02')
router.register(r'taskListPPM02ByCompany', CompanyCodeTaskListPPM02ViewSet, basename='companyCode-taskListPPM02')
router.register(r'taskListAPM02', TaskListAPM02ViewSet, basename='taskListAPM02')
router.register(r'taskListAPM02ByCompany', CompanyCodeTaskListAPM02ViewSet, basename='companyCode-taskListAPM02')

router.register(r'taskListPPM03', TaskListPPM03ViewSet, basename='taskListPPM03')
router.register(r'taskListPPM03ByCompany', CompanyCodeTaskListPPM03ViewSet, basename='companyCode-taskListPPM03')
router.register(r'taskListAPM03', TaskListAPM03ViewSet, basename='taskListAPM03')
router.register(r'taskListAPM03ByCompany', CompanyCodeTaskListAPM03ViewSet, basename='companyCode-taskListAPM03')

router.register(r'taskListPPM04', TaskListPPM04ViewSet, basename='taskListPPM04')
router.register(r'taskListPPM04ByCompany', CompanyCodeTaskListPPM04ViewSet, basename='companyCode-taskListPPM04')

router.register(r'taskListPPM05', TaskListPPM05ViewSet, basename='taskListPPM05')
router.register(r'taskListPPM05ByCompany', CompanyCodeTaskListPPM05ViewSet, basename='companyCode-taskListPPM05')
router.register(r'taskListAPM05', TaskListAPM05ViewSet, basename='taskListAPM05')
router.register(r'taskListAPM05ByCompany', CompanyCodeTaskListAPM05ViewSet, basename='companyCode-taskListAPM05')

urlpatterns = [
    path('task/', include(router.urls)),
]
