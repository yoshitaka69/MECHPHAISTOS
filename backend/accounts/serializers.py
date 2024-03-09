from rest_framework import serializers
from .models import Company,CustomUser,Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment # 呼び出すモデル
        fields = '__all__' # API上に表示するモデルのデータ項目


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company # 呼び出すモデル
        fields = '__all__' # API上に表示するモデルのデータ項目


class CustomUserSerializer(serializers.ModelSerializer):
    companyCode = CompanySerializer()
    class Meta:
        model = CustomUser
        fields = '__all__'