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

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import MasterDataTable, CompanyCode
from .serializers import MasterDataTableSerializer
from django.db.models import Max

class MasterDataTableViewSet(viewsets.ModelViewSet):
    queryset = MasterDataTable.objects.all()
    serializer_class = MasterDataTableSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        # デバッグ用: 受信したデータを確認
        print("Received data:", data)

        # データがリストであることを確認
        if not isinstance(data, list):
            return Response({"error": "Expected a list but got a different type."}, status=status.HTTP_400_BAD_REQUEST)

        # 送信されたceListNoのリストを作成
        sent_ce_list_nos = [item.get('ceListNo') for item in data if item.get('ceListNo') is not None]

        # 現在のデータベースに存在するceListNoを取得
        existing_ce_list_nos = list(MasterDataTable.objects.values_list('ceListNo', flat=True))

        # 削除する必要があるceListNoを特定
        ce_list_nos_to_delete = set(existing_ce_list_nos) - set(sent_ce_list_nos)

        # 削除処理
        if ce_list_nos_to_delete:
            MasterDataTable.objects.filter(ceListNo__in=ce_list_nos_to_delete).delete()

        # 新規作成または更新の処理
        created_items = []
        for item in data:
            company_code_str = item.get('companyCode')

            # companyCodeが文字列として渡された場合、それに対応するオブジェクトを取得
            try:
                company_code_obj = CompanyCode.objects.get(companyCode=company_code_str)
                item['companyCode'] = company_code_obj.id  # IDに変換
            except CompanyCode.DoesNotExist:
                return Response(
                    {"error": f"CompanyCode '{company_code_str}' does not exist."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            ce_list_no = item.get('ceListNo')

            if ce_list_no is not None:
                # ceListNoが存在する場合、既存のレコードを更新する
                existing_item = MasterDataTable.objects.filter(ceListNo=ce_list_no).first()
                if existing_item:
                    serializer = self.get_serializer(existing_item, data=item, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    created_items.append(serializer.data)
                    continue  # 更新処理をした場合は次のアイテムに進む

            # ceListNoがnullまたは新規作成の場合
            if ce_list_no is None:
                # 最大のceListNoを取得し、そこから次の番号を割り当てる
                max_ce_list_no = MasterDataTable.objects.aggregate(Max('ceListNo'))['ceListNo__max'] or "00000"
                max_ce_list_no = int(max_ce_list_no)  # 整数に変換
                item['ceListNo'] = str(max_ce_list_no + 1).zfill(5)  # 整数を文字列に変換してゼロ埋め

            serializer = self.get_serializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            created_items.append(serializer.data)

        return Response(created_items, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        ce_list_no = request.data.get('ceListNo')
        if ce_list_no:
            try:
                # ceListNoに基づいて既存の製品を取得し、削除を試みる
                master_data = MasterDataTable.objects.get(ceListNo=ce_list_no)
                self.perform_destroy(master_data)
                print("Delete request received with ceListNo:", ce_list_no)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except MasterDataTable.DoesNotExist:
                return Response({"error": "Master Data Table with ceListNo not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "ceListNo not provided."}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()









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
    





#-------------------------------------------------------------------------------------------------------------------


from rest_framework import viewsets
from .models import ScheduleForGantt
from .serializers import ScheduleForGanttSerializer,CompanyCodeScheduleForGanttSerializer

class ScheduleForGanttViewSet(viewsets.ModelViewSet):
    queryset = ScheduleForGantt.objects.all()
    serializer_class = ScheduleForGanttSerializer
    

class CompanyCodeScheduleForGanttViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeScheduleForGanttSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('scheduleForGantt_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset

#-------------------------------------------------------------------------------------------------------------------


from rest_framework import viewsets
from .models import ScheduleForCalendar
from .serializers import ScheduleForCalendarSerializer,CompanyCodeScheduleForCalendarSerializer

from rest_framework import viewsets
from .models import ScheduleForCalendar
from .serializers import ScheduleForCalendarSerializer
from rest_framework.response import Response
from rest_framework import status

class ScheduleForCalendarViewSet(viewsets.ModelViewSet):
    queryset = ScheduleForCalendar.objects.all()
    serializer_class = ScheduleForCalendarSerializer

    def create(self, request, *args, **kwargs):
        # リクエストからデータを取得
        data = request.data
        company_code_str = data.get('companyCode')

        # companyCode の処理
        try:
            company_code_obj = CompanyCode.objects.get(companyCode=company_code_str)
            data['companyCode'] = company_code_obj.id  # IDを設定
        except CompanyCode.DoesNotExist:
            return Response(
                {"error": f"CompanyCode '{company_code_str}' does not exist."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # シリアライザを使ってデータを保存
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, *args, **kwargs):
        # eventDataNoで特定のイベントを取得
        eventDataNo = kwargs.get('pk')
        instance = ScheduleForCalendar.objects.get(eventDataNo=eventDataNo)

        # シリアライザで更新処理
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)




class CompanyCodeScheduleForCalendarViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeScheduleForCalendarSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('scheduleForCalendar_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset