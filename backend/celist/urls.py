from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CeListViewSet, CeListByCompanyViewSet, post_risk_matrix_possibility, get_latest_risk_matrix_possibilities, post_risk_matrix_impact, get_latest_risk_matrix_impacts

router = DefaultRouter()
router.register(r'ceList', CeListViewSet, basename='ceList')
router.register(r'ceListByCompany', CeListByCompanyViewSet, basename='companyCode-ceList')

urlpatterns = [
    path('ceList/', include(router.urls)),
    path('ceList/risk_matrix_possibility/', post_risk_matrix_possibility, name='add_risk_matrix_possibility'),
    path('ceList/risk_matrix_possibility/<str:company_code>/', get_latest_risk_matrix_possibilities, name='get_latest_risk_matrix_possibilities'),
    path('ceList/risk_matrix_impact/', post_risk_matrix_impact, name='add_risk_matrix_impact'),
    path('ceList/risk_matrix_impact/<str:company_code>/<str:level_set_value>/', get_latest_risk_matrix_impacts, name='get_latest_risk_matrix_impacts'),
]


#Django REST FrameworkのViewSetと単一の関数ベースビュー（FBV）を組み合わせるためには、URLルーティングを少し変更する必要があります。
#post_risk_matrix_possibilityはViewSetではなく関数ベースビューなので、router.registerではなく、直接URLパスを定義する必要がある。