from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


from .models import CeList,CompanyCode,Plant,Equipment,Machine,TypeOfPM
from .serializers import CeSerializer,CompanyCodeCeSerializer,PlantSerializer,EquipmentSerializer,MachineSerializer,TypeOfPMSerializer

class PlantListViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class EquipmentListViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class MachineListViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class TypeOfPMListViewSet(viewsets.ModelViewSet):
    queryset = TypeOfPM.objects.all()
    serializer_class = TypeOfPMSerializer

#Critical equipment list
class CeListViewSet(viewsets.ModelViewSet):
    queryset = CeList.objects.all()
    serializer_class = CeSerializer

class CeListByCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CeSerializer

    def get_queryset(self):
        companyCode_slug = self.kwargs['companyCode_slug']
        return CeList.objects.filter(companyCode__slug=companyCode_slug)

@api_view(['GET'])
def company_ce_list(request):
    companies = CompanyCode.objects.all()
    serializer = CompanyCodeCeSerializer(companies, many=True)
    return Response(serializer.data)


