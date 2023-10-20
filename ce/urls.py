from django.urls import path
from ce.views import CeAPIView

from django.views.generic import TemplateView
#from .views import DataTableView #Datatable追加部分
from . import views


urlpatterns = [
        path("ce-api/", CeAPIView.as_view(), name="Critical_Equipment_API"),#APIのurls


        #path('ce-base/', views.ceBase, name='Crtical_Equipment_Base'),
        #path('ce-list/', views.ceDisplay, name='Crtical_Equipment_List'),
        #path('ce-listdatatables/', TemplateView.as_view(template_name='ceListdatatables.html'), name='Crtical_Equipment_Datatables'), #追加部分
        #path('data/', DataTableView.as_view()), #追加部分
]