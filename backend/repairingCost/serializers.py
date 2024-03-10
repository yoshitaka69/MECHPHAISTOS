from rest_framework import serializers
from .models import PlannedPM02,ActualPM02,PlannedPM03,ActualPM03,ActualPM04,PlannedPM05,ActualPM05


class PlannedPM02Serializer(serializers.ModelSerializer):
    plannedMonth = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = PlannedPM02 # 呼び出すモデル
        fields = '__all__' # API上に表示するモデルのデータ項目
class ActualPM02Serializer(serializers.ModelSerializer):
    actualMonth = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = ActualPM02
        fields = '__all__'


class PlannedPM03Serializer(serializers.ModelSerializer):
    plannedMonth = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = PlannedPM03
        fields = '__all__' 
class ActualPM03Serializer(serializers.ModelSerializer):
    actualMonth = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = ActualPM03
        fields = '__all__'



class ActualPM04Serializer(serializers.ModelSerializer):
    actualMonth = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = ActualPM04
        fields = '__all__'


class PlannedPM05Serializer(serializers.ModelSerializer):
    plannedMonth = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = PlannedPM03
        fields = '__all__' 
class ActualPM05Serializer(serializers.ModelSerializer):
    actualMonth = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = ActualPM03
        fields = '__all__'