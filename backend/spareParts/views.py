from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .models import SpareParts,Category,Location,Classification
from accounts.models import CompanyCode
from .serializers import SparePartsSerializer,CategorySerializer,LocationSerializer,ClassificationSerializer,CompanyCodeSPSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


#SparePartsList
class SparePartsViewSet(viewsets.ModelViewSet):
    queryset = SpareParts.objects.all()
    serializer_class = SparePartsSerializer

class CompanyCodeSPViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeSPSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('spareParts_companyCode').all()#ここでのrelatedNameの間違いは要注意