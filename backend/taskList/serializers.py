from rest_framework import serializers
from .models import TaskList,Company
from datetime import timedelta, datetime


class TaskSerializer(serializers.ModelSerializer):
    nextEventDate = serializers.DateField(read_only=True)
    situation = models.CharField(read_only=True)
                                         
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
        company_code = validated_data.get('company', {}).get('companyCode', '')
        last_task = TaskList.objects.filter(taskCode__startswith=company_code).order_by('-taskCode').first()

        if last_task:
            last_number = int(last_task.taskCode[len(company_code):])  # company_codeを取り除いて整数化
            new_task_code_number = last_number + 1
        else:
            new_task_code_number = 1

        validated_data['taskCode'] = f'{company_code}{str(new_task_code_number).zfill(3)}'
        return TaskList.objects.create(**validated_data)


class CompanyTaskSerializer(serializers.ModelSerializer):
    taskList = TaskSerializer(many=True, read_only=True, source='task_set')

    class Meta:
        model = Company
        fields = ['companyCode', 'taskList']

