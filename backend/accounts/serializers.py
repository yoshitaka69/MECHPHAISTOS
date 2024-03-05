from rest_framework import serializers
from .models import Company,Payment,CustomUser


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment # 呼び出すモデル
        fields = [
            "freeUser",
            "lightUser",
            'middleUser',
            "specialUser",
            "premiumUser",
        ] # API上に表示するモデルのデータ項目

class CompanySerializer(serializers.ModelSerializer):
    payment = PaymentSerializer()
    class Meta:
        model = Company # 呼び出すモデル
        fields = [
            "payment",
            "companyCode",
            "companyListNo",
            "companyName",
            'country',
            "zipCode",
            "payment",
            "createdDay",
            "updateDay",
        ] # API上に表示するモデルのデータ項目
\


class CustomUserSerializer(serializers.ModelSerializer):
    companyCode = CompanySerializer()
    payment = PaymentSerializer()

    class Meta:
        model = CustomUser
        fields = [
            "payment",
            "companyCode",
            "userName",
            "firstName",
            'familyName',
            'email',
            "phoneNumber",
            'company',
            'payment',
            'is_active',
            'is_staff',
            "createdDay",
            "updateDay",
            ]