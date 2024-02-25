from rest_framework import serializers
from .models import Company,User,Payment


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company # 呼び出すモデル
        fields = [
            "companyListNo",
            "companyName",
            'country',
            "zipCode",
            "accountType",
            "createdDay",
            "updateDay",
        ] # API上に表示するモデルのデータ項目



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # 呼び出すモデル
        fields = [
            "userName",
            "firstName",
            'familyName',
            "email",
            "phoneNumber",
            "createdDay",
            "updateDay",
        ] # API上に表示するモデルのデータ項目


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment # 呼び出すモデル
        fields = [
            "companyCode",
            "companyName",
            'country',
            "zipCode",
            "accountType",
            "createdDay",
            "updateDay",
        ] # API上に表示するモデルのデータ項目
