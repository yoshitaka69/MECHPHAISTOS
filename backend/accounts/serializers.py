from rest_framework import serializers
from .models import Company,UserInfo,Payment,CustomUser


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



class UserInfoSerializer(serializers.ModelSerializer):
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

class CustomUserSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    user_info = UserInfoSerializer()
    payment = PaymentSerializer()

    class Meta:
        model = CustomUser
        fields = ['email', 'company', 'user_info', 'payment', 'is_active', 'is_staff', 'date_joined']