from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


from .models import Ce,Company
from .serializers import CeSerializer,CompanyCeSerializer


#Critical equipment list
class CeViewSet(viewsets.ModelViewSet):
    queryset = Ce.objects.all()
    serializer_class = CeSerializer

class CeByCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CeSerializer

    def get_queryset(self):
        companyCode_slug = self.kwargs['companyCode_slug']
        return Ce.objects.filter(companyCode__slug=companyCode_slug)

@api_view(['GET'])
def company_ce_list(request):
    companies = Company.objects.all()
    serializer = CompanyCeSerializer(companies, many=True)
    return Response(serializer.data)


