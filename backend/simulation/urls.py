from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import No1SimulationAPIView,No2SimulationAPIView,No3SimulationAPIView,CompanyCodeNo1SimulationListView,CompanyCodeNo2SimulationListView,CompanyCodeNo3SimulationListView



router = DefaultRouter()


router.register(r'no1simulations', No1SimulationAPIView,basename='no1simulations')
router.register(r'no1simulationsByCompany', CompanyCodeNo1SimulationListView, basename='companyCode-no1simulations')
router.register(r'no2simulations', No2SimulationAPIView,basename='no2simulations')
router.register(r'no2simulationsByCompany', CompanyCodeNo2SimulationListView, basename='companyCode-no2simulations')
router.register(r'no3simulations', No3SimulationAPIView,basename='no3simulations')
router.register(r'no3simulationsByCompany', CompanyCodeNo3SimulationListView, basename='companyCode-no3simulations')


urlpatterns = [
    path('simulation/', include(router.urls)),
]