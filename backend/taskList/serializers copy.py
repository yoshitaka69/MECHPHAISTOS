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
        fields = ["companyCode","companyName","plant","equipment","machineName","taskCode","taskName","laborCostOfPPM02","countOfPPM02","latestPPM02","periodOfPPM02","constructionPeriod","nextEventDate","situation","thisYear","thisYear1later","thisYear2later","thisYear3later","thisYear4later","thisYear5later","thisYear6later","thisYear7later","thisYear8later","thisYear9later","thisYear10later",]# API上に表示するモデルのデータ項目
        

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
        fields = ["companyCode","companyName","plant","equipment","machineName","taskCode","taskName","laborCostOfPPM03","countOfPPM03","latestPPM03","periodOfPPM03","constructionPeriod","nextEventDate","situation","thisYear","thisYear1later","thisYear2later","thisYear3later","thisYear4later","thisYear5later","thisYear6later","thisYear7later","thisYear8later","thisYear9later","thisYear10later",]# API上に表示するモデルのデータ項目
        

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
        fields = ["taskCode", 'typicalTaskName', 'typicalTaskCode', 'typicalLatestDate', 'typicalConstPeriod', 'typicalNextEventDate', 'multiTasking','typicalSituation']# API上に表示するモデルのデータ項目
        
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



class TaskListSerializer(serializers.ModelSerializer):
    companyCode = create_slug_related_field('companyCode', CompanyCode.objects.all())
    plant = create_slug_related_field('plant', Plant.objects.all())
    equipment = create_slug_related_field('equipment', Equipment.objects.all())
    machineName = create_slug_related_field('machineName', Machine.objects.all())
    typicalLatestDate = create_slug_related_field('typicalLatestDate', TypicalTaskList.objects.all())
    typicalTaskName = create_slug_related_field('typicalTaskName', TypicalTaskList.objects.all())
    typicalTaskCost = create_slug_related_field('typicalTaskCost', TypicalTaskList.objects.all())
    typicalConstPeriod = create_slug_related_field('typicalConstPeriod', TypicalTaskList.objects.all())
    multiTasking = create_slug_related_field('multiTasking', TypicalTaskList.objects.all())
    typicalNextEventDate = create_slug_related_field('typicalNextEventDate', TypicalTaskList.objects.all())
    typicalSituation = create_slug_related_field('typicalSituation', TypicalTaskList.objects.all())

    bomCode = create_slug_related_field('bomCode', TypicalTaskList.objects.all())
    bomCost = create_slug_related_field('bomCost', TypicalTaskList.objects.all())

    
    class Meta:
        model = TaskList #呼び出すモデル名
        fields = ["companyCode", 'plant', 'equipment', 'machineName', 'taskListNo', 'typicalLatestDate', 'typicalTaskName', 'typicalTaskCost', 'typicalConstPeriod', 'multiTasking', 'typicalNextEventDate', 'typicalSituation', 'bomCode', 'bomCost', 'totalCost', 'thisYear', 'thisYear1later', 'thisYear2later', 'thisYear3later', 'thisYear4later', 'thisYear5later', 'thisYear6later', 'thisYear7later', 'thisYear8later', 'thisYear9later', 'thisYear10later', ]# API上に表示するモデルのデータ項目


class CompanyTaskListSerializer(serializers.ModelSerializer):
    taskList = TaskListSerializer(many=True, read_only=True, source='taskList_companyCode')#ここのsourceは注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'taskList']
