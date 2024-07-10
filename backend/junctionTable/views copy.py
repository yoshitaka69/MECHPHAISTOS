from django.shortcuts import render
from rest_framework import viewsets

from .models import MasterDataTable,BomAndTask,CeListAndTask,BadActorManagement,EventYearPPM,GapOfRepairingCost
from accounts.models import CompanyCode
from .serializers import  (MasterDataTableSerializer, CompanyCodeMDTSerializer,
                           BomAndTaskSerializer,CompanyCodeBomAndTaskSerializer,
                           CeListAndTaskSerializer,CompanyCodeCeListAndTaskSerializer,
                           BadActorManagementSerializer,CompanyCodeBadActorSerializer,
                           EventYearPPMSerializer,CompanyCodeEventYearPPMSerializer,
                           GapOfRepairingCostSerializer,CompanyCodeGapOfRepairingCostSerializer,)




#-------------------------------------------------------------------------------------------------------------------


from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MasterDataTable, CompanyCode, Plant, Equipment, Machine
from .serializers import MasterDataTableSerializer
from django.db import transaction

# MasterDataTable
class MasterDataTableViewSet(viewsets.ModelViewSet):
    queryset = MasterDataTable.objects.all()
    serializer_class = MasterDataTableSerializer

@api_view(['GET', 'POST'])
def master_data_table_by_company(request):
    if request.method == 'GET':
        company_code = request.query_params.get('companyCode')
        if company_code:
            try:
                company_code_obj = CompanyCode.objects.get(companyCode=company_code)
                data = MasterDataTable.objects.filter(companyCode=company_code_obj)
                serializer = MasterDataTableSerializer(data, many=True)
                return Response(serializer.data)
            except CompanyCode.DoesNotExist:
                return Response({'error': 'Invalid companyCode'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'companyCode is required'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        company_code = request.data.get('companyCode')
        master_data = request.data.get('MasterDataTable')

        if not company_code or not master_data:
            return Response({'error': 'companyCode and MasterDataTable are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                # CompanyCodeの存在確認と作成
                company_code_obj, created = CompanyCode.objects.get_or_create(companyCode=company_code)

                for data in master_data:
                    data['companyCode'] = company_code_obj

                    # Plantの存在確認と作成
                    plant_name = data.pop('plant', None)
                    if plant_name:
                        plant_obj, created = Plant.objects.get_or_create(plant=plant_name)
                        data['plant'] = plant_obj

                    # Equipmentの存在確認と作成
                    equipment_name = data.pop('equipment', None)
                    if equipment_name:
                        equipment_obj, created = Equipment.objects.get_or_create(equipment=equipment_name)
                        data['equipment'] = equipment_obj

                    # Machineの存在確認と作成
                    machine_name = data.pop('machineName', None)
                    if machine_name:
                        machine_obj, created = Machine.objects.get_or_create(name=machine_name)
                        data['machineName'] = machine_obj

                    ce_list_no = data.pop('ceListNo')
                    obj, created = MasterDataTable.objects.update_or_create(
                        companyCode=company_code_obj,
                        ceListNo=ce_list_no,
                        defaults=data
                    )
                serializer = MasterDataTableSerializer(MasterDataTable.objects.filter(companyCode=company_code_obj), many=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CompanyCodeMDTViewSet(viewsets.ViewSet):
    def list(self, request):
        company_code = request.query_params.get('companyCode')
        if company_code:
            try:
                company_code_obj = CompanyCode.objects.get(companyCode=company_code)
                data = MasterDataTable.objects.filter(companyCode=company_code_obj)
                serializer = MasterDataTableSerializer(data, many=True)
                return Response(serializer.data)
            except CompanyCode.DoesNotExist:
                return Response({'error': 'Invalid companyCode'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'companyCode is required'}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        company_code = request.data.get('companyCode')
        master_data = request.data.get('MasterDataTable')

        if not company_code or not master_data:
            return Response({'error': 'companyCode and MasterDataTable are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                company_code_obj, created = CompanyCode.objects.get_or_create(companyCode=company_code)

                for data in master_data:
                    data['companyCode'] = company_code_obj

                    # Plantの存在確認と作成
                    plant_name = data.pop('plant', None)
                    if plant_name:
                        plant_obj, created = Plant.objects.get_or_create(plant=plant_name)
                        data['plant'] = plant_obj

                    # Equipmentの存在確認と作成
                    equipment_name = data.pop('equipment', None)
                    if equipment_name:
                        equipment_obj, created = Equipment.objects.get_or_create(equipment=equipment_name)
                        data['equipment'] = equipment_obj

                    # Machineの存在確認と作成
                    machine_name = data.pop('machineName', None)
                    if machine_name:
                        machine_obj, created = Machine.objects.get_or_create(name=machine_name)
                        data['machineName'] = machine_obj

                    ce_list_no = data.pop('ceListNo')
                    obj, created = MasterDataTable.objects.update_or_create(
                        companyCode=company_code_obj,
                        ceListNo=ce_list_no,
                        defaults=data
                    )
                serializer = MasterDataTableSerializer(MasterDataTable.objects.filter(companyCode=company_code_obj), many=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('masterDataTable_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset










#-------------------------------------------------------------------------------------------------------------------




#BomAndTask
class BomAndTaskViewSet(viewsets.ModelViewSet):
    queryset = BomAndTask.objects.all()
    serializer_class = BomAndTaskSerializer


class CompanyCodeBomAndTaskViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeBomAndTaskSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('bomAndTask_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset





#CeListAndTask
class CeListAndTaskViewSet(viewsets.ModelViewSet):
    queryset = CeListAndTask.objects.all()
    serializer_class = CeListAndTaskSerializer


class CompanyCodeCeListAndTaskViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeCeListAndTaskSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('ceListAndTask_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset




#BadActorManagement
class BadActorManagementViewSet(viewsets.ModelViewSet):
    queryset = BadActorManagement.objects.all()
    serializer_class = BadActorManagementSerializer

class CompanyCodeBadActorViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeBadActorSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('badActorManagement_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset




class EventYearPPMViewSet(viewsets.ModelViewSet):
    queryset = EventYearPPM.objects.all()
    serializer_class = EventYearPPMSerializer

class CompanyCodeEventYearPPMViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeEventYearPPMSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('eventYearPPM_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
    




class GapOfRepairingCostViewSet(viewsets.ModelViewSet):
    queryset = GapOfRepairingCost.objects.all()
    serializer_class = GapOfRepairingCostSerializer

class CompanyCodeGapOfRepairingCostViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeGapOfRepairingCostSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('gapOfRepairingCost_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset