from rest_framework import serializers
from .models import CompanyList,UserList,PaymentsList


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyList # 呼び出すモデル
        fields = [
            "companyListNo",
            "companyName",
            'country',
            "zipCode",
            "accountType",
            "createdDay",
            "updateDay",
        ] # API上に表示するモデルのデータ項目



class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserList # 呼び出すモデル
        fields = [
            "userName",
            "firstName",
            'familyName',
            "email",
            "phoneNumber",
            "createdDay",
            "updateDay",
        ] # API上に表示するモデルのデータ項目


class PaymentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsList # 呼び出すモデル
        fields = [
            "companyCode",
            "companyName",
            'country',
            "zipCode",
            "accountType",
            "createdDay",
            "updateDay",
        ] # API上に表示するモデルのデータ項目
