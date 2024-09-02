from rest_framework import viewsets

from rest_framework.pagination import PageNumberPagination
from accounts.models import CompanyCode
from .models import TaskListPPM02,TaskListAPM02,TaskListPPM03,TaskListAPM03,TaskListAPM04,TaskListPPM05,TaskListAPM05,TypicalTaskList,TaskList
from .serializers import (TaskListPPM02Serializer,CompanyTaskListPPM02Serializer,
                          TaskListAPM02Serializer,CompanyTaskListAPM02Serializer,

                          TaskListPPM03Serializer,CompanyTaskListPPM03Serializer,
                          TaskListAPM03Serializer,CompanyTaskListAPM03Serializer,

                          TaskListAPM04Serializer,CompanyTaskListAPM04Serializer,

                          TaskListPPM05Serializer,CompanyTaskListPPM05Serializer,
                          TaskListAPM05Serializer,CompanyTaskListAPM05Serializer,

                          TypicalTaskListSerializer,CompanyTypicalTaskListSerializer,
                          TaskListSerializer,CompanyTaskListSerializer)



#TasKListPPM02
class TaskListPPM02ViewSet(viewsets.ModelViewSet):
    queryset = TaskListPPM02.objects.all()
    serializer_class = TaskListPPM02Serializer

class CompanyCodeTaskListPPM02ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListPPM02Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListPPM02_companyCode').all()
    


#TaskListAPM02
class TaskListAPM02ViewSet(viewsets.ModelViewSet):
    queryset = TaskListAPM02.objects.all()
    serializer_class = TaskListAPM02Serializer

class CompanyCodeTaskListAPM02ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListAPM02Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListAPM02_companyCode').all()





#TaskListPPM03
class TaskListPPM03ViewSet(viewsets.ModelViewSet):
    queryset = TaskListPPM03.objects.all()
    serializer_class = TaskListPPM03Serializer

class CompanyCodeTaskListPPM03ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListPPM03Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListPPM03_companyCode').all()



#TaskListAPM03
class TaskListAPM03ViewSet(viewsets.ModelViewSet):
    queryset = TaskListAPM03.objects.all()
    serializer_class = TaskListAPM03Serializer

class CompanyCodeTaskListAPM03ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListAPM03Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListAPM03_companyCode').all()




#TaskListAPM04
class TaskListAPM04ViewSet(viewsets.ModelViewSet):
    queryset = TaskListAPM04.objects.all()
    serializer_class = TaskListAPM04Serializer

class CompanyCodeTaskListAPM04ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListAPM04Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListAPM04_companyCode').all()




#TaskListPPM05
class TaskListPPM05ViewSet(viewsets.ModelViewSet):
    queryset = TaskListPPM05.objects.all()
    serializer_class = TaskListPPM05Serializer

class CompanyCodeTaskListPPM05ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListPPM05Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListPPM05_companyCode').all()



#TaskListAPM05
class TaskListAPM05ViewSet(viewsets.ModelViewSet):
    queryset = TaskListAPM05.objects.all()
    serializer_class = TaskListAPM05Serializer

class CompanyCodeTaskListAPM05ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListAPM05Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListAPM05_companyCode').all()





#TypicalTaskList
class TypicalTaskListViewSet(viewsets.ModelViewSet):
    queryset = TypicalTaskList.objects.all()
    serializer_class = TypicalTaskListSerializer

class CompanyCodeTypicalTaskListViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTypicalTaskListSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('typicalTaskList_companyCode').all()
    



#-------------------------------------------------------------



#TaskList
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Max
from .models import TaskList, CompanyCode
from .serializers import TaskListSerializer

class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        # データがリストでない場合、リストに変換
        if not isinstance(data, list):
            data = [data]

        sent_task_list_nos = [item.get('taskListNo') for item in data if item.get('taskListNo') is not None]

        # 現在のデータベースに存在するtaskListNoを取得
        existing_task_list_nos = list(TaskList.objects.values_list('taskListNo', flat=True))

        # 削除する必要があるtaskListNoを特定
        task_list_nos_to_delete = set(existing_task_list_nos) - set(sent_task_list_nos)

        # 削除処理
        if task_list_nos_to_delete:
            TaskList.objects.filter(taskListNo__in=task_list_nos_to_delete).delete()

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

            task_list_no = item.get('taskListNo')

            if task_list_no is not None:
                # taskListNoが存在する場合、既存のレコードを更新する
                existing_item = TaskList.objects.filter(taskListNo=task_list_no).first()
                if existing_item:
                    serializer = self.get_serializer(existing_item, data=item, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    created_items.append(serializer.data)
                    continue  # 更新処理をした場合は次のアイテムに進む

            # taskListNoがnullまたは新規作成の場合
            if task_list_no is None:
                # 最大のtaskListNoを取得し、そこから次の番号を割り当てる
                max_task_list_no = TaskList.objects.aggregate(Max('taskListNo'))['taskListNo__max'] or "00000"
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
                task_list = TaskList.objects.get(taskListNo=task_list_no)
                self.perform_destroy(task_list)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except TaskList.DoesNotExist:
                return Response({"error": f"Task List with taskListNo '{task_list_no}' not found."},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "taskListNo not provided."}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()








class CompanyCodeTaskListViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListSerializer

    def get_queryset(self):
        company_code = self.request.query_params.get('companyCode', None)
        if company_code is not None:
            return CompanyCode.objects.filter(companyCode=company_code).prefetch_related('taskList_companyCode')
        return CompanyCode.objects.all()


#-------------------------------------------------------------
