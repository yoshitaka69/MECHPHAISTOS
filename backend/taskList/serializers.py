from rest_framework import serializers
from .models import TaskListPPM02,TaskListAPM02,TaskListPPM03,TaskListAPM03,TaskListAPM04,TaskListPPM05,TaskListAPM05,TypicalTaskList,TaskList
from accounts.models import CompanyCode,Plant
from ceList.models import Equipment,Machine
from datetime import timedelta, datetime




class TaskListPPM02Serializer(serializers.ModelSerializer):
    nextEventDate = serializers.DateField(read_only=True)
    situation = serializers.CharField(read_only=True)

    thisYear10ago = serializers.BooleanField(read_only=True)
    thisYear9ago = serializers.BooleanField(read_only=True)
    thisYear8ago = serializers.BooleanField(read_only=True)
    thisYear7ago = serializers.BooleanField(read_only=True)
    thisYear6ago = serializers.BooleanField(read_only=True)
    thisYear5ago = serializers.BooleanField(read_only=True)
    thisYear4ago = serializers.BooleanField(read_only=True)
    thisYear3ago = serializers.BooleanField(read_only=True)
    thisYear2ago = serializers.BooleanField(read_only=True)
    thisYear1ago = serializers.BooleanField(read_only=True)

    thisYear1later = serializers.BooleanField(read_only=True)
    thisYear2later = serializers.BooleanField(read_only=True)
    thisYear3later = serializers.BooleanField(read_only=True)
    thisYear4later = serializers.BooleanField(read_only=True)
    thisYear5later = serializers.BooleanField(read_only=True)
    thisYear6later = serializers.BooleanField(read_only=True)
    thisYear7later = serializers.BooleanField(read_only=True)
    thisYear8later = serializers.BooleanField(read_only=True)
    thisYear9later = serializers.BooleanField(read_only=True)
    thisYear10later = serializers.BooleanField(read_only=True)


    class Meta:
        model = TaskListPPM02 #呼び出すモデル名
        fields = ["companyCode","companyName","plant","equipment","machineName","taskCode","taskName","laborCostOfPPM02","countOfPPM02","latestPPM02","periodOfPPM02", "pM02Content", "maintenanceCategory","constructionPeriod","nextEventDate","situation","thisYear10ago","thisYear9ago","thisYear8ago","thisYear7ago","thisYear6ago","thisYear5ago","thisYear4ago","thisYear3ago","thisYear2ago","thisYear1ago","thisYear","thisYear1later","thisYear2later","thisYear3later","thisYear4later","thisYear5later","thisYear6later","thisYear7later","thisYear8later","thisYear9later","thisYear10later",]# API上に表示するモデルのデータ項目
        

    #situationを判定する関数
    def validate(self, data):
        latest_pm = data.get('latestPM')
        period_of_pm = data.get('periodOfPM')

        if latest_pm and period_of_pm is not None:
            # Calculate nextEventDate
            calculated_next_event_date = latest_pm + timedelta(days=period_of_pm)
            data['nextEventDate'] = calculated_next_event_date

            # 現在の日付を取得
            current_date = datetime.now().date()

            # nextEventDateと現在の日付を比較してsituationを設定
            if calculated_next_event_date < current_date:
                data['situation'] = ''
            elif calculated_next_event_date > current_date:
                data['situation'] = '遅延'
        
        return data



        
class CompanyTaskListPPM02Serializer(serializers.ModelSerializer):
    taskListPPM02 = TaskListPPM02Serializer(many=True, read_only=True, source='taskListPPM02_companyCode')#ここのsourceは注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'taskListPPM02']









#ActualPM02
class TaskListAPM02Serializer(serializers.ModelSerializer):
    class Meta:
        model = TaskListAPM02
        field = ['companyCode','companyName','plant','equipment','machineName','taskCode','taskName','laborCostOfAPM02','startDateAPM02','endDateAPM02','constructionPeriod','description']

class CompanyTaskListAPM02Serializer(serializers.ModelSerializer):
   taskListAPM02 = TaskListAPM02Serializer(many=True, read_only=True, source='taskListAPM02_companyCode')#ここのsourceは注意
   class Meta:
        model = CompanyCode
        fields = ['companyCode', 'taskListAPM02']







#planned PM03
class TaskListPPM03Serializer(serializers.ModelSerializer):
    nextEventDate = serializers.DateField(read_only=True)
    situation = serializers.CharField(read_only=True)

    thisYear10ago = serializers.BooleanField(read_only=True)
    thisYear9ago = serializers.BooleanField(read_only=True)
    thisYear8ago = serializers.BooleanField(read_only=True)
    thisYear7ago = serializers.BooleanField(read_only=True)
    thisYear6ago = serializers.BooleanField(read_only=True)
    thisYear5ago = serializers.BooleanField(read_only=True)
    thisYear4ago = serializers.BooleanField(read_only=True)
    thisYear3ago = serializers.BooleanField(read_only=True)
    thisYear2ago = serializers.BooleanField(read_only=True)
    thisYear1ago = serializers.BooleanField(read_only=True)

    thisYear1later = serializers.BooleanField(read_only=True)
    thisYear2later = serializers.BooleanField(read_only=True)
    thisYear3later = serializers.BooleanField(read_only=True)
    thisYear4later = serializers.BooleanField(read_only=True)
    thisYear5later = serializers.BooleanField(read_only=True)
    thisYear6later = serializers.BooleanField(read_only=True)
    thisYear7later = serializers.BooleanField(read_only=True)
    thisYear8later = serializers.BooleanField(read_only=True)
    thisYear9later = serializers.BooleanField(read_only=True)
    thisYear10later = serializers.BooleanField(read_only=True)


    class Meta:
        model = TaskListPPM03 #呼び出すモデル名
        fields = ["companyCode","companyName","plant","equipment","machineName","taskCode","taskName","laborCostOfPPM03","countOfPPM03","latestPPM03","periodOfPPM03","pM03Content", "maintenanceCategory","constructionPeriod","nextEventDate","situation","thisYear10ago","thisYear9ago","thisYear8ago","thisYear7ago","thisYear6ago","thisYear5ago","thisYear4ago","thisYear3ago","thisYear2ago","thisYear1ago","thisYear","thisYear1later","thisYear2later","thisYear3later","thisYear4later","thisYear5later","thisYear6later","thisYear7later","thisYear8later","thisYear9later","thisYear10later",]# API上に表示するモデルのデータ項目
        

    #situationを判定する関数
    def validate(self, data):
        latest_pm = data.get('latestPM')
        period_of_pm = data.get('periodOfPM')

        if latest_pm and period_of_pm is not None:
            # Calculate nextEventDate
            calculated_next_event_date = latest_pm + timedelta(days=period_of_pm)
            data['nextEventDate'] = calculated_next_event_date

            # 現在の日付を取得
            current_date = datetime.now().date()

            # nextEventDateと現在の日付を比較してsituationを設定
            if calculated_next_event_date < current_date:
                data['situation'] = ''
            elif calculated_next_event_date > current_date:
                data['situation'] = '遅延'
        
        return data
    


        # nextEventDateとthisYearXlaterフィールドの設定
        instance = TaskListPM03.objects.create(**validated_data)

        latest_pm = validated_data.get('latestPM')
        period_pm = validated_data.get('periodPM', 0)
        current_year = datetime.now().year
        instance.thisYear = str(current_year)

        if latest_pm:
            # latestPM が提供されている場合、1年後から10年後までの日付を計算
            for i in range(1, 11):
                next_event_date = latest_pm + timedelta(days=period_pm * i)
                if next_event_date.year - current_year == i:
                    setattr(instance, f'thisYear{i}later', True)
                else:
                    setattr(instance, f'thisYear{i}later', False)
        else:
            # latestPM が提供されていない場合、全てのフィールドを False に設定
            for i in range(1, 11):
                setattr(instance, f'thisYear{i}later', False)

        instance.save()
        return instance
class CompanyTaskListPPM03Serializer(serializers.ModelSerializer):
    taskListPPM03 = TaskListPPM03Serializer(many=True, read_only=True, source='taskListPPM03_companyCode')#ここのsourceは注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'taskListPPM03']






#ActualPM03
class TaskListAPM03Serializer(serializers.ModelSerializer):
    class Meta:
        model = TaskListAPM03
        field = ['companyCode','companyName','plant','equipment','machineName','taskCode','taskName','laborCostOfAPM03','startDateAPM03','endDateAPM03','constructionPeriod','description']

class CompanyTaskListAPM03Serializer(serializers.ModelSerializer):
   taskListAPM03 = TaskListAPM03Serializer(many=True, read_only=True, source='taskListAPM03_companyCode')#ここのsourceは注意
   
   class Meta:
        model = CompanyCode
        fields = ['companyCode', 'taskListAPM03']








#ActualPM04
class TaskListAPM04Serializer(serializers.ModelSerializer):
    class Meta:
        model = TaskListAPM04 #呼び出すモデル名
        fields = ["companyCode","companyName","plant","equipment","machineName","taskCode","taskName","laborCostOfAPM04","countOfAPM04","latestAPM04","constructionPeriod",]# API上に表示するモデルのデータ項目

class CompanyTaskListAPM04Serializer(serializers.ModelSerializer):
    taskList = TaskListAPM04Serializer(many=True, read_only=True, source='taskListPM4_companyCode')#ここのsourceは注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'taskList']







#Planned PM05
class TaskListPPM05Serializer(serializers.ModelSerializer):
    nextEventDate = serializers.DateField(read_only=True)
    situation = serializers.CharField(read_only=True)

    thisYear10ago = serializers.BooleanField(read_only=True)
    thisYear9ago = serializers.BooleanField(read_only=True)
    thisYear8ago = serializers.BooleanField(read_only=True)
    thisYear7ago = serializers.BooleanField(read_only=True)
    thisYear6ago = serializers.BooleanField(read_only=True)
    thisYear5ago = serializers.BooleanField(read_only=True)
    thisYear4ago = serializers.BooleanField(read_only=True)
    thisYear3ago = serializers.BooleanField(read_only=True)
    thisYear2ago = serializers.BooleanField(read_only=True)
    thisYear1ago = serializers.BooleanField(read_only=True)

    thisYear1later = serializers.BooleanField(read_only=True)
    thisYear2later = serializers.BooleanField(read_only=True)
    thisYear3later = serializers.BooleanField(read_only=True)
    thisYear4later = serializers.BooleanField(read_only=True)
    thisYear5later = serializers.BooleanField(read_only=True)
    thisYear6later = serializers.BooleanField(read_only=True)
    thisYear7later = serializers.BooleanField(read_only=True)
    thisYear8later = serializers.BooleanField(read_only=True)
    thisYear9later = serializers.BooleanField(read_only=True)
    thisYear10later = serializers.BooleanField(read_only=True)


    class Meta:
        model = TaskListPPM05 #呼び出すモデル名
        fields = ["companyCode","companyName","plant","equipment","machineName","taskCode","taskName","laborCostOfPPM05","countOfPPM05","latestPPM05","periodOfPPM05","constructionPeriod","nextEventDate","situation","thisYear","thisYear1later","thisYear2later","thisYear3later","thisYear4later","thisYear5later","thisYear6later","thisYear7later","thisYear8later","thisYear9later","thisYear10later",]# API上に表示するモデルのデータ項目
        

    #situationを判定する関数
    def validate(self, data):
        latest_pm = data.get('latestPM')
        period_of_pm = data.get('periodOfPM')

        if latest_pm and period_of_pm is not None:
            # Calculate nextEventDate
            calculated_next_event_date = latest_pm + timedelta(days=period_of_pm)
            data['nextEventDate'] = calculated_next_event_date

            # 現在の日付を取得
            current_date = datetime.now().date()

            # nextEventDateと現在の日付を比較してsituationを設定
            if calculated_next_event_date < current_date:
                data['situation'] = ''
            elif calculated_next_event_date > current_date:
                data['situation'] = '遅延'
        
        return data


        # nextEventDateとthisYearXlaterフィールドの設定
        instance = TaskListPM05.objects.create(**validated_data)

        latest_pm = validated_data.get('latestPM')
        period_pm = validated_data.get('periodPM', 0)
        current_year = datetime.now().year
        instance.thisYear = str(current_year)

        if latest_pm:
            # latestPM が提供されている場合、1年後から10年後までの日付を計算
            for i in range(1, 11):
                next_event_date = latest_pm + timedelta(days=period_pm * i)
                if next_event_date.year - current_year == i:
                    setattr(instance, f'thisYear{i}later', True)
                else:
                    setattr(instance, f'thisYear{i}later', False)
        else:
            # latestPM が提供されていない場合、全てのフィールドを False に設定
            for i in range(1, 11):
                setattr(instance, f'thisYear{i}later', False)

        instance.save()
        return instance


class CompanyTaskListPPM05Serializer(serializers.ModelSerializer):
    taskListPPM05 = TaskListPPM05Serializer(many=True, read_only=True, source='taskListPPM05_companyCode')#ここのsourceは注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'taskListPPM05']



#ActualPM05
class TaskListAPM05Serializer(serializers.ModelSerializer):
    class Meta:
        model = TaskListAPM05
        field = ['companyCode','companyName','plant','equipment','machineName','taskCode','taskName','laborCostOfAPM05','startDateAPM05','endDateAPM05','constructionPeriod','description']

class CompanyTaskListAPM05Serializer(serializers.ModelSerializer):
   taskListAPM05 = TaskListAPM05Serializer(many=True, read_only=True, source='taskListAPM05_companyCode')#ここのsourceは注意
   class Meta:
        model = CompanyCode
        fields = ['companyCode', 'taskListAPM05']








#typicalTaskList
class TypicalTaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypicalTaskList #呼び出すモデル名
        fields = ["taskCode", 'typicalTaskName', 'typicalLatestDate', 'typicalConstPeriod', 'typicalNextEventDate', 'multiTasking','typicalSituation']# API上に表示するモデルのデータ項目
        
class CompanyTypicalTaskListSerializer(serializers.ModelSerializer):
    typicalTaskList = TypicalTaskListSerializer(many=True, read_only=True, source='typicalTaskList_companyCode')#ここのsourceは注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'typicalTaskList']


#TaskList

#ForeignKeyを文字列で返すslugフィールを関数化する。
def create_slug_related_field(field_name, queryset):
    return serializers.SlugRelatedField(
        slug_field=field_name, 
        queryset=queryset
    )




#-------------------------------------------------------

from rest_framework import serializers
from .models import TaskList, CompanyCode, Plant, Equipment, Machine, TypicalTaskList, BomList

class TaskListSerializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode',
        queryset=CompanyCode.objects.all()
    )
    plant = serializers.SlugRelatedField(
        slug_field='plant',
        queryset=Plant.objects.all(),
        allow_null=True,
        required=False
    )
    equipment = serializers.SlugRelatedField(
        slug_field='equipment',
        queryset=Equipment.objects.all(),
        allow_null=True,
        required=False
    )
    machineName = serializers.SlugRelatedField(
        slug_field='machineName',
        queryset=Machine.objects.all(),
        allow_null=True,
        required=False
    )
    typicalLatestDatePM = serializers.SlugRelatedField(
        slug_field='taskCode',
        queryset=TypicalTaskList.objects.all(),
        allow_null=True,
        required=False
    )
    typicalTaskName = serializers.SlugRelatedField(
        slug_field='taskCode',
        queryset=TypicalTaskList.objects.all(),
        allow_null=True,
        required=False
    )
    typicalTaskCost = serializers.SlugRelatedField(
        slug_field='taskCode',
        queryset=TypicalTaskList.objects.all(),
        allow_null=True,
        required=False
    )
    typicalConstPeriod = serializers.SlugRelatedField(
        slug_field='taskCode',
        queryset=TypicalTaskList.objects.all(),
        allow_null=True,
        required=False
    )
    multiTasking = serializers.SlugRelatedField(
        slug_field='taskCode',
        queryset=TypicalTaskList.objects.all(),
        allow_null=True,
        required=False
    )
    typicalNextEventDate = serializers.SlugRelatedField(
        slug_field='taskCode',
        queryset=TypicalTaskList.objects.all(),
        allow_null=True,
        required=False
    )
    typicalSituation = serializers.SlugRelatedField(
        slug_field='taskCode',
        queryset=TypicalTaskList.objects.all(),
        allow_null=True,
        required=False
    )
    bomCode = serializers.SlugRelatedField(
        slug_field='taskCode',
        queryset=BomList.objects.all(),
        allow_null=True,
        required=False
    )
    bomCost = serializers.SlugRelatedField(
        slug_field='taskCode',
        queryset=BomList.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = TaskList
        fields = [
            'companyCode', 'plant', 'equipment', 'machineName', 'taskListNo',
            'typicalLatestDatePM', 'typicalTaskName', 'typicalTaskCost', 'typicalConstPeriod',
            'multiTasking', 'typicalNextEventDate', 'typicalSituation', 'bomCode', 'bomCost',
            'totalCost', 'thisYear', 'thisYear1later', 'thisYear2later', 'thisYear3later',
            'thisYear4later', 'thisYear5later', 'thisYear6later', 'thisYear7later',
            'thisYear8later', 'thisYear9later', 'thisYear10later'
        ]

    def to_internal_value(self, data):
        equipment_data = data.get('equipment')
        machine_name_data = data.get('machineName')
        typical_latest_date_pm_data = data.get('typicalLatestDatePM')

        if equipment_data and not Equipment.objects.filter(equipment=equipment_data).exists():
            data['equipment'] = Equipment.objects.create(equipment=equipment_data).equipment

        if machine_name_data and not Machine.objects.filter(machineName=machine_name_data).exists():
            data['machineName'] = Machine.objects.create(machineName=machine_name_data).machineName

        if typical_latest_date_pm_data and not TypicalTaskList.objects.filter(taskCode=typical_latest_date_pm_data).exists():
            data['typicalLatestDatePM'] = TypicalTaskList.objects.create(taskCode=typical_latest_date_pm_data).taskCode

        return super().to_internal_value(data)



class CompanyTaskListSerializer(serializers.ModelSerializer):
    taskList = TaskListSerializer(many=True, source='taskList_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'taskList']

    def create(self, validated_data):
        task_list_data = validated_data.pop('taskList_companyCode')
        company_code_instance = CompanyCode.objects.get(companyCode=validated_data['companyCode'])
        
        for task_data in task_list_data:
            company_code_str = task_data.pop('companyCode')
            company_code_instance = CompanyCode.objects.get(companyCode=company_code_str)

            task_list_no = task_data.get('taskListNo')
            task_instance = TaskList.objects.filter(companyCode=company_code_instance, taskListNo=task_list_no).first()

            if task_instance:
                # 更新
                serializer = TaskListSerializer(task_instance, data=task_data)
                if serializer.is_valid():
                    serializer.save()
            else:
                # taskListNoを自動生成
                existing_task_nos = TaskList.objects.values_list('taskListNo', flat=True).order_by('taskListNo')
                existing_task_nos_int = [int(taskListNo) for taskListNo in existing_task_nos if taskListNo.isdigit()]
                if existing_task_nos_int:
                    missing_no = next((i for i in range(1, max(existing_task_nos_int) + 2) if i not in existing_task_nos_int), None)
                    task_list_no = missing_no if missing_no is not None else max(existing_task_nos_int) + 1
                else:
                    task_list_no = 1

                task_data['taskListNo'] = str(task_list_no)  # taskListNoを文字列として保存

                # すべてのフィールドが空欄またはnullでないことを確認（orderSituationを除外）
                if any(value for key, value in task_data.items() if key != 'orderSituation'):
                    TaskList.objects.create(companyCode=company_code_instance, **task_data)
        
        return company_code_instance

    def update(self, instance, validated_data):
        task_list_data = validated_data.pop('taskList_companyCode')
        existing_tasks = TaskList.objects.filter(companyCode=instance)

        # 更新するタスクリストの管理
        task_list_no_list = [task['taskListNo'] for task in task_list_data]

        # 削除するタスクを特定
        for existing_task in existing_tasks:
            if existing_task.taskListNo not in task_list_no_list:
                existing_task.delete()

        for task_data in task_list_data:
            task_list_no = task_data.get('taskListNo')
            task_instance = TaskList.objects.filter(companyCode=instance, taskListNo=task_list_no).first()
            
            if task_instance:
                # 更新
                serializer = TaskListSerializer(task_instance, data=task_data)
                if serializer.is_valid():
                    serializer.save()
            else:
                # 新規作成
                company_code_str = task_data.pop('companyCode')
                company_code_instance = CompanyCode.objects.get(companyCode=company_code_str)
                task_data['companyCode'] = company_code_instance

                # taskListNoを自動生成
                existing_task_nos = TaskList.objects.values_list('taskListNo', flat=True).order_by('taskListNo')
                existing_task_nos_int = [int(taskListNo) for taskListNo in existing_task_nos if taskListNo.isdigit()]
                if existing_task_nos_int:
                    missing_no = next((i for i in range(1, max(existing_task_nos_int) + 2) if i not in existing_task_nos_int), None)
                    task_list_no = missing_no if missing_no is not None else max(existing_task_nos_int) + 1
                else:
                    task_list_no = 1

                task_data['taskListNo'] = str(task_list_no)

                # すべてのフィールドが空欄またはnullでないことを確認（orderSituationを除外）
                if any(value for key, value in task_data.items() if key != 'orderSituation'):
                    TaskList.objects.create(**task_data)
        
        instance.save()
        return instance




#-------------------------------------------------------