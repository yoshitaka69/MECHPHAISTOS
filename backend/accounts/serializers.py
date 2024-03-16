from rest_framework import serializers
from .models import Company,CustomUser,Payment,CompanyCode,CompanyName,AreaCode,CommunityGroup

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment # 呼び出すモデル
        fields = '__all__' # API上に表示するモデルのデータ項目

class CompanyCodeSerializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = CompanyCode
        fields = '__all__'

class CompanyNameSerializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = CompanyName
        fields = '__all__'

class AreaCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaCode
        fields = '__all__'


class CommunityGroupSerializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = CommunityGroup
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = Company
        fields = '__all__'





#CustomUserSerializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['userName','email','payment']

class CompanyCodeUserSerializer(serializers.ModelSerializer):
    users = CustomUserSerializer(many=True, read_only=True, source='customUser_companyCode')  # sourceはCustomUserモデルのrelated_name
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'users']