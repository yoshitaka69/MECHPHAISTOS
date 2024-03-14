from rest_framework import serializers
from .models import TaskList,CompanyCode
from datetime import timedelta, datetime



class TaskSerializer(serializers.ModelSerializer):
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
        model = TaskList #呼び出すモデル名
        fields = '__all__'# API上に表示するモデルのデータ項目
        
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
    


    def create(self, validated_data):
        # taskCodeの生成
        company_code = validated_data.get('company', {}).get('companyCode', '')
        last_task = TaskList.objects.filter(taskCode__startswith=company_code).order_by('-taskCode').first()

        if last_task:
            last_number = int(last_task.taskCode[len(company_code):])
            new_task_code_number = last_number + 1
        else:
            new_task_code_number = 1

        validated_data['taskCode'] = f'{company_code}{str(new_task_code_number).zfill(3)}'


        # nextEventDateとthisYearXlaterフィールドの設定
        instance = TaskList.objects.create(**validated_data)

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


class CompanyTaskSerializer(serializers.ModelSerializer):
    taskList = TaskSerializer(many=True, read_only=True, source='taskList_companyCode')#ここのsourceは注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'taskList']

