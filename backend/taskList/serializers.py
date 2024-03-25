from rest_framework import serializers
from .models import TaskListPM02,TaskListPM03,TaskListPM04,TaskListPM05,TypicalTaskList,TaskList
from accounts.models import CompanyCode
from datetime import timedelta, datetime




class TaskListPM02Serializer(serializers.ModelSerializer):
    taskCode = serializers.CharField(read_only=True)
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
        model = TaskListPM02 #呼び出すモデル名
        fields = ["companyCode","companyName","plant","equipment","machineName","taskCode","taskName","laborCostOfPM","countOfPM","latestPM","periodOfPM","constructionPeriod","nextEventDate","situation","thisYear","thisYear1later","thisYear2later","thisYear3later","thisYear4later","thisYear5later","thisYear6later","thisYear7later","thisYear8later","thisYear9later","thisYear10later",]# API上に表示するモデルのデータ項目
        

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
    

    # taskCodeの生成
    def create(self, validated_data):
        
        company_code = validated_data.get('company', {}).get('companyCode', '')
        last_task = TaskListPM02.objects.filter(taskCode__startswith=company_code).order_by('-taskCode').first()

        if last_task:
            last_number = int(last_task.taskCode[len(company_code):])
            new_task_code_number = last_number + 1
        else:
            new_task_code_number = 1

        validated_data['taskCode'] = f'{company_code}{str(new_task_code_number).zfill(3)}'


        # nextEventDateとthisYearXlaterフィールドの設定
        instance = TaskListPM02.objects.create(**validated_data)

        latest_pm = validated_data.get('latestPM')
        period_pm = validated_data.get('periodPM', 0)
        current_year = datetime.now().year
        instance.thisYear = str(current_year)

        if latest_pm:
            for i in range(1, 11):
                next_event_date = latest_pm + timedelta(days=period_pm * i)
                # ここでの条件は、計算されたイベント日付が現在の年数 + i年に該当するかどうかをチェック
                if next_event_date.year <= current_year + i:
                    setattr(instance, f'thisYear{i}later', True)
                else:
                    setattr(instance, f'thisYear{i}later', False)
        else:
            # latestPM が提供されていない場合、全てのフィールドを False に設定
            for i in range(1, 11):
                setattr(instance, f'thisYear{i}later', False)

        instance.save()
        return instance



class CompanyTaskListPM02Serializer(serializers.ModelSerializer):
    taskList = TaskListPM02Serializer(many=True, read_only=True, source='taskListPM02_companyCode')#ここのsourceは注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'taskList']








class TaskListPM03Serializer(serializers.ModelSerializer):
    taskCode = serializers.CharField(read_only=True)
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
        model = TaskListPM03 #呼び出すモデル名
        fields = ["companyCode","companyName","plant","equipment","machineName","taskCode","taskName","laborCostOfPM","countOfPM","latestPM","periodOfPM","constructionPeriod","nextEventDate","situation","thisYear","thisYear1later","thisYear2later","thisYear3later","thisYear4later","thisYear5later","thisYear6later","thisYear7later","thisYear8later","thisYear9later","thisYear10later",]# API上に表示するモデルのデータ項目
        

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
    
    # taskCodeの生成
    def create(self, validated_data):
        
        company_code = validated_data.get('company', {}).get('companyCode', '')
        last_task = TaskListPM03.objects.filter(taskCode__startswith=company_code).order_by('-taskCode').first()

        if last_task:
            last_number = int(last_task.taskCode[len(company_code):])
            new_task_code_number = last_number + 1
        else:
            new_task_code_number = 1

        validated_data['taskCode'] = f'{company_code}{str(new_task_code_number).zfill(3)}'


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


class CompanyTaskListPM03Serializer(serializers.ModelSerializer):
    taskList = TaskListPM03Serializer(many=True, read_only=True, source='taskListPM03_companyCode')#ここのsourceは注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'taskList']



class TaskListPM04Serializer(serializers.ModelSerializer):
    taskCode = serializers.CharField(read_only=True)

    class Meta:
        model = TaskListPM04 #呼び出すモデル名
        fields = ["companyCode","companyName","plant","equipment","machineName","taskCode","taskName","laborCostOfPM","countOfPM","latestPM","constructionPeriod",]# API上に表示するモデルのデータ項目
        
    
    # taskCodeの生成
    def create(self, validated_data):
        
        company_code = validated_data.get('company', {}).get('companyCode', '')
        last_task = TaskListPM04.objects.filter(taskCode__startswith=company_code).order_by('-taskCode').first()

        if last_task:
            last_number = int(last_task.taskCode[len(company_code):])
            new_task_code_number = last_number + 1
        else:
            new_task_code_number = 1

        validated_data['taskCode'] = f'{company_code}{str(new_task_code_number).zfill(3)}'


class CompanyTaskListPM04Serializer(serializers.ModelSerializer):
    taskList = TaskListPM04Serializer(many=True, read_only=True, source='taskListPM4_companyCode')#ここのsourceは注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'taskList']










class TaskListPM05Serializer(serializers.ModelSerializer):
    taskCode = serializers.CharField(read_only=True)
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
        model = TaskListPM05 #呼び出すモデル名
        fields = ["companyCode","companyName","plant","equipment","machineName","taskCode","taskName","laborCostOfPM","countOfPM","latestPM","periodOfPM","constructionPeriod","nextEventDate","situation","thisYear","thisYear1later","thisYear2later","thisYear3later","thisYear4later","thisYear5later","thisYear6later","thisYear7later","thisYear8later","thisYear9later","thisYear10later",]# API上に表示するモデルのデータ項目
        

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
    
    # taskCodeの生成
    def create(self, validated_data):
        
        company_code = validated_data.get('company', {}).get('companyCode', '')
        last_task = TaskListPM05.objects.filter(taskCode__startswith=company_code).order_by('-taskCode').first()

        if last_task:
            last_number = int(last_task.taskCode[len(company_code):])
            new_task_code_number = last_number + 1
        else:
            new_task_code_number = 1

        validated_data['taskCode'] = f'{company_code}{str(new_task_code_number).zfill(3)}'


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


class CompanyTaskListPM05Serializer(serializers.ModelSerializer):
    taskList = TaskListPM05Serializer(many=True, read_only=True, source='taskListPM05_companyCode')#ここのsourceは注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'taskList']



#typicalTaskList
class TypicalTaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypicalTaskList #呼び出すモデル名
        fields = ["taskCode", 'typicalTaskName', 'typicalTaskCode', 'typicalLatestDate', 'typicalConstPeriod', 'typicalNextEventDate', 'multiTasking']# API上に表示するモデルのデータ項目
        
class CompanyTypicalTaskListSerializer(serializers.ModelSerializer):
    typicalTaskList = TypicalTaskListSerializer(many=True, read_only=True, source='typicalTaskList_companyCode')#ここのsourceは注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'typicalTaskList']


#TaskList

class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskList #呼び出すモデル名
        fields = ["companyCode", 'plant', 'equipment', 'machineName', 'taskListNo', 'typicalLatestDate', 'typicalTaskName', 'typicalTaskCost', 'typicalConstPeriod', 'multiTasking', 'typicalNextEventDate', 'typicalSituation', 'bomCode', 'bomCost', 'totalCost', 'thisYear', 'thisYear1later', 'thisYear2later', 'thisYear3later', 'thisYear4later', 'thisYear5later', 'thisYear6later', 'thisYear7later', 'thisYear8later', 'thisYear9later', 'thisYear10later', ]# API上に表示するモデルのデータ項目


class CompanyTaskListSerializer(serializers.ModelSerializer):
    taskList = TaskListSerializer(many=True, read_only=True, source='taskList_companyCode')#ここのsourceは注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'taskList']