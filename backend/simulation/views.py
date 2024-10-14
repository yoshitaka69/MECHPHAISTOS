from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import No1Simulation, No2Simulation, No3Simulation
from .serializers import (
    CompanyCodeNo1SimulationSerializer,
    CompanyCodeNo2SimulationSerializer,
    CompanyCodeNo3SimulationSerializer,
    No1SimulationSerializer,
    No2SimulationSerializer,
    No3SimulationSerializer
)
from accounts.models import CompanyCode





#------------------------------------------------------------
# No1Simulationの新規作成、取得、更新、削除のためのビュー
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Max
from .models import No1Simulation, CompanyCode
from .serializers import No1SimulationSerializer, CompanyCodeNo1SimulationSerializer

class No1SimulationAPIView(viewsets.ModelViewSet):
    queryset = No1Simulation.objects.all()
    serializer_class = No1SimulationSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        # データがリストでない場合、リストに変換
        if not isinstance(data, list):
            data = [data]

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

            # 既存のシミュレーションレコードがあるか確認
            task_list_no = item.get('taskListNo')
            if task_list_no is not None:
                # taskListNoが存在する場合、既存のレコードを更新する
                existing_item = No1Simulation.objects.filter(taskListNo=task_list_no).first()
                if existing_item:
                    serializer = self.get_serializer(existing_item, data=item, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    created_items.append(serializer.data)
                    continue  # 更新処理をした場合は次のアイテムに進む

            # taskListNoがnullまたは新規作成の場合
            if task_list_no is None:
                # 最大のtaskListNoを取得し、そこから次の番号を割り当てる
                max_task_list_no = No1Simulation.objects.aggregate(Max('taskListNo'))['taskListNo__max'] or "00000"
                max_task_list_no = int(max_task_list_no)  # 整数に変換
                item['taskListNo'] = str(max_task_list_no + 1).zfill(5)  # 整数を文字列に変換してゼロ埋め

            serializer = self.get_serializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            created_items.append(serializer.data)

        return Response(created_items, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        task_list_no = request.data.get('taskListNo')
        if task_list_no:
            try:
                # taskListNoに基づいて既存のデータを取得し、削除を試みる
                simulation = No1Simulation.objects.get(taskListNo=task_list_no)
                self.perform_destroy(simulation)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except No1Simulation.DoesNotExist:
                return Response({"error": f"Simulation with taskListNo '{task_list_no}' not found."},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "taskListNo not provided."}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

# CompanyCodeに関連するNo1Simulationリストを取得
class CompanyCodeNo1SimulationListView(viewsets.ModelViewSet):
    serializer_class = CompanyCodeNo1SimulationSerializer

    def get_queryset(self):
        company_code = self.request.query_params.get('companyCode', None)
        if company_code is not None:
            return CompanyCode.objects.filter(companyCode=company_code).prefetch_related('no1Simulation_companyCode')
        return CompanyCode.objects.all()



#------------------------------------------------------------




#------------------------------------------------------------

# No2Simulationの新規作成、取得、更新、削除のためのビュー
class No2SimulationAPIView(viewsets.ModelViewSet):
    queryset = No2Simulation.objects.all()
    serializer_class = No2SimulationSerializer  # ここでserializer_classを指定

    def create(self, request, *args, **kwargs):
        data = request.data

        # データがリストでない場合、リストに変換
        if not isinstance(data, list):
            data = [data]

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

            # 既存のシミュレーションレコードがあるか確認
            task_list_no = item.get('taskListNo')
            if task_list_no is not None:
                # taskListNoが存在する場合、既存のレコードを更新する
                existing_item = No2Simulation.objects.filter(taskListNo=task_list_no).first()
                if existing_item:
                    serializer = self.get_serializer(existing_item, data=item, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    created_items.append(serializer.data)
                    continue  # 更新処理をした場合は次のアイテムに進む

            # taskListNoがnullまたは新規作成の場合
            if task_list_no is None:
                # 最大のtaskListNoを取得し、そこから次の番号を割り当てる
                max_task_list_no = No2Simulation.objects.aggregate(Max('taskListNo'))['taskListNo__max'] or "00000"
                max_task_list_no = int(max_task_list_no)  # 整数に変換
                item['taskListNo'] = str(max_task_list_no + 1).zfill(5)  # 整数を文字列に変換してゼロ埋め

            serializer = self.get_serializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            created_items.append(serializer.data)

        return Response(created_items, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        task_list_no = request.data.get('taskListNo')
        if task_list_no:
            try:
                # taskListNoに基づいて既存のデータを取得し、削除を試みる
                simulation = No2Simulation.objects.get(taskListNo=task_list_no)
                self.perform_destroy(simulation)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except No2Simulation.DoesNotExist:
                return Response({"error": f"Simulation with taskListNo '{task_list_no}' not found."},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "taskListNo not provided."}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

# CompanyCodeに関連するNo2Simulationリストを取得
class CompanyCodeNo2SimulationListView(viewsets.ModelViewSet):
    serializer_class = CompanyCodeNo2SimulationSerializer

    def get_queryset(self):
        company_code = self.request.query_params.get('companyCode', None)
        if company_code is not None:
            return CompanyCode.objects.filter(companyCode=company_code).prefetch_related('no2Simulation_companyCode')
        return CompanyCode.objects.all()

#------------------------------------------------------------




#------------------------------------------------------------

# No3Simulationの新規作成、取得、更新、削除のためのビュー
class No3SimulationAPIView(viewsets.ModelViewSet):
    queryset = No3Simulation.objects.all()
    serializer_class = No3SimulationSerializer  # ここでserializer_classを指定

    def create(self, request, *args, **kwargs):
        data = request.data

        # データがリストでない場合、リストに変換
        if not isinstance(data, list):
            data = [data]

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

            # 既存のシミュレーションレコードがあるか確認
            task_list_no = item.get('taskListNo')
            if task_list_no is not None:
                # taskListNoが存在する場合、既存のレコードを更新する
                existing_item = No3Simulation.objects.filter(taskListNo=task_list_no).first()
                if existing_item:
                    serializer = self.get_serializer(existing_item, data=item, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    created_items.append(serializer.data)
                    continue  # 更新処理をした場合は次のアイテムに進む

            # taskListNoがnullまたは新規作成の場合
            if task_list_no is None:
                # 最大のtaskListNoを取得し、そこから次の番号を割り当てる
                max_task_list_no = No3Simulation.objects.aggregate(Max('taskListNo'))['taskListNo__max'] or "00000"
                max_task_list_no = int(max_task_list_no)  # 整数に変換
                item['taskListNo'] = str(max_task_list_no + 1).zfill(5)  # 整数を文字列に変換してゼロ埋め

            serializer = self.get_serializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            created_items.append(serializer.data)

        return Response(created_items, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        task_list_no = request.data.get('taskListNo')
        if task_list_no:
            try:
                # taskListNoに基づいて既存のデータを取得し、削除を試みる
                simulation = No3Simulation.objects.get(taskListNo=task_list_no)
                self.perform_destroy(simulation)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except No3Simulation.DoesNotExist:
                return Response({"error": f"Simulation with taskListNo '{task_list_no}' not found."},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "taskListNo not provided."}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

# CompanyCodeに関連するNo3Simulationリストを取得
class CompanyCodeNo3SimulationListView(viewsets.ModelViewSet):
    serializer_class = CompanyCodeNo3SimulationSerializer

    def get_queryset(self):
        company_code = self.request.query_params.get('companyCode', None)
        if company_code is not None:
            return CompanyCode.objects.filter(companyCode=company_code).prefetch_related('no3Simulation_companyCode')
        return CompanyCode.objects.all()

    
#------------------------------------------------------------