from django.urls import path
from accounts import views


urlpatterns = [
    path('companyList/', views.CompanyListView.as_view()),
    path('companyList/userList', views.UserListView.as_view()),
    path('companyList/paymentsList', views.PaymentsListView.as_view()),
]