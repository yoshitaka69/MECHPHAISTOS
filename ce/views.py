from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

#Datatable---------
'''
from django.http import HttpResponse
from .models import CeList #datatable表示model
from django_datatables_view.base_datatable_view import BaseDatatableView
'''
#Datatable---------



#API表示------------
class CeAPIView(APIView):


    def get(self, request):
        return Response("OK", status=status.HTTP_200_OK)
    
class IndexView(TemplateView):#Index表示させるだけのclass

    template_name = "index.html"
#ここまでAPI表示--------------









#Datatable表示views----------
'''
def ceBase(request):
    return render(request, 'CeBase.html')

def ceDisplay(request):
    data = CeList.objects.all()
    contents = {'data': data}
    return render(request, 'CeDisplay.html', contents)


class DataTableView(BaseDatatableView):
    # モデルの指定cd
    model = CeList
    # 表示するフィールドの指定
    columns = ['book_name', 'author', 'publisher', 'price']

    # 検索方法の指定：部分一致
    def get_filter_method(self):
        return super().FILTER_ICONTAINS
    
'''
#ここまでDatatable表示views----------



