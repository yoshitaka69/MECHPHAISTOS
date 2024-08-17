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
from rest_framework.response import Response
from .models import MasterDataTable, CompanyCode, Plant, Equipment, Machine, CeList
from .serializers import MasterDataTableSerializer
import logging

logger = logging.getLogger(__name__)

class MasterDataTableViewSet(viewsets.ModelViewSet):
    queryset = MasterDataTable.objects.all()
    serializer_class = MasterDataTableSerializer

    def create(self, request, *args, **kwargs):
        data_list = request.data.get('MasterDataTable', [])
        logger.info(f"Received data: {data_list}")

        for data in data_list:
            company_code_str = request.data.get('companyCode')
            logger.debug(f"Processing companyCode: {company_code_str}")
            company_code, _ = CompanyCode.objects.get_or_create(companyCode=company_code_str)

            # Plantインスタンスを取得または作成
            plant_value = data.get('plant')
            plant_instance = None
            if plant_value:
                plant_instance, _ = Plant.objects.get_or_create(plant=plant_value, companyCode=company_code)
                logger.debug(f"Plant instance: {plant_instance}")

            # Equipmentインスタンスを取得または作成
            equipment_value = data.get('equipment')
            equipment_instance = None
            if equipment_value:
                equipment_instance, _ = Equipment.objects.get_or_create(equipment=equipment_value, companyCode=company_code, plant=plant_instance)
                logger.debug(f"Equipment instance: {equipment_instance}")

            # Machineインスタンスを取得または作成
            machine_name_value = data.get('machineName')
            machine_instance = None
            if machine_name_value:
                machine_instance, _ = Machine.objects.get_or_create(machineName=machine_name_value, companyCode=company_code)
                logger.debug(f"Machine instance: {machine_instance}")

            # CeList インスタンスを取得または作成
            ce_list_instance = CeList.objects.create(
                companyCode=company_code,
                plant=plant_instance,
                equipment=equipment_instance,
                machineName=machine_instance
            )

            # データを保存
            master_data = MasterDataTable.objects.create(
                companyCode=company_code,
                ceListNo=ce_list_instance,
                plant=plant_instance,
                equipment=equipment_instance,
                machineName=machine_instance,
                levelSetValue=data.get('levelSetValue'),
                mttr=data.get('mttr'),
                probabilityOfFailure=data.get('probabilityOfFailure'),
                countOfPM02=data.get('countOfPM02'),
                latestPM02=data.get('latestPM02'),
                countOfPM03=data.get('countOfPM03'),
                latestPM03=data.get('latestPM03'),
                countOfPM04=data.get('countOfPM04'),
                latestPM04=data.get('latestPM04'),
                impactForProduction=data.get('impactForProduction'),
                assessment=data.get('assessment'),
                rcaOrReplace=data.get('rcaOrReplace'),
                sparePartsOrAlternative=data.get('sparePartsOrAlternative'),
                coveredFromTask=data.get('coveredFromTask'),
                twoways=data.get('twoways'),
                ceDescription=data.get('ceDescription'),
            )
            logger.info(f"Data saved: {master_data}")

        return Response({"status": "success"}, status=201)

    def update(self, request, *args, **kwargs):
        master_data_table = self.get_object()
        logger.info(f"Updating MasterDataTable with ID: {master_data_table.id}")

        # companyCodeのみ処理
        company_code_str = request.data.pop('companyCode')
        company_code, _ = CompanyCode.objects.get_or_create(companyCode=company_code_str)
        master_data_table.companyCode = company_code
        
        # 他のフィールドも更新
        master_data_table.plant = request.data.get('plant', master_data_table.plant)
        master_data_table.equipment = request.data.get('equipment', master_data_table.equipment)
        master_data_table.machineName = request.data.get('machineName', master_data_table.machineName)
        master_data_table.levelSetValue = request.data.get('levelSetValue', master_data_table.levelSetValue)
        master_data_table.mttr = request.data.get('mttr', master_data_table.mttr)
        master_data_table.probabilityOfFailure = request.data.get('probabilityOfFailure', master_data_table.probabilityOfFailure)
        master_data_table.countOfPM02 = request.data.get('countOfPM02', master_data_table.countOfPM02)
        master_data_table.latestPM02 = request.data.get('latestPM02', master_data_table.latestPM02)
        master_data_table.countOfPM03 = request.data.get('countOfPM03', master_data_table.countOfPM03)
        master_data_table.latestPM03 = request.data.get('latestPM03', master_data_table.latestPM03)
        master_data_table.countOfPM04 = request.data.get('countOfPM04', master_data_table.countOfPM04)
        master_data_table.latestPM04 = request.data.get('latestPM04', master_data_table.latestPM04)
        master_data_table.impactForProduction = request.data.get('impactForProduction', master_data_table.impactForProduction)
        master_data_table.assessment = request.data.get('assessment', master_data_table.assessment)
        master_data_table.rcaOrReplace = request.data.get('rcaOrReplace', master_data_table.rcaOrReplace)
        master_data_table.sparePartsOrAlternative = request.data.get('sparePartsOrAlternative', master_data_table.sparePartsOrAlternative)
        master_data_table.coveredFromTask = request.data.get('coveredFromTask', master_data_table.coveredFromTask)
        master_data_table.twoways = request.data.get('twoways', master_data_table.twoways)
        master_data_table.ceDescription = request.data.get('ceDescription', master_data_table.ceDescription)

        master_data_table.save()
        logger.info(f"MasterDataTable updated: {master_data_table}")
        serializer = self.get_serializer(master_data_table)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        master_data_table = self.get_object()
        logger.info(f"Deleting MasterDataTable with ID: {master_data_table.id}")
        master_data_table.delete()
        return Response(status=204)
















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

                    plant_name = data.pop('plant', None)
                    if plant_name:
                        plant_obj, created = Plant.objects.get_or_create(plant=plant_name)
                        data['plant'] = plant_obj

                    equipment_name = data.pop('equipment', None)
                    if equipment_name:
                        equipment_obj, created = Equipment.objects.get_or_create(equipment=equipment_name)
                        data['equipment'] = equipment_obj

                    machine_name = data.pop('machineName', None)
                    if machine_name:
                        machine_obj, created = Machine.objects.get_or_create(machineName=machine_name)
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