from rest_framework import serializers
from .models import Company,CustomUser,Payment,CompanyCode,CompanyName,AreaCode,CommunityGroup,Plant

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment # 呼び出すモデル
        fields = ['paymentType','description'] # API上に表示するモデルのデータ項目

class CompanyCodeSerializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = CompanyCode
        fields = ['companyCode','description','createDay']

class CompanyNameSerializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = CompanyName
        fields = ['companyCode','companyName','description','createDay']



class AreaCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaCode
        fields = ['companyCode','companyName','country','zipCode','description']


class CommunityGroupSerializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = CommunityGroup
        fields = ['companyCode','companyName','communityGroup','createDay','updateDay']


class CompanySerializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = Company
        fields = ['companyCode','companyListNo','companyName','country','zipCode','payment','communityGroup','createDay','updateDay']






class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['companyCode', 'plant']

    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode', 
        queryset=CompanyCode.objects.all()
    )

    

class CompanyPlantSerializer(serializers.ModelSerializer):
    plantList = PlantSerializer(many=True, source='plant_companyCode')  
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plantList']




#CustomUserSerializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"





class CompanyCodeUserSerializer(serializers.ModelSerializer):
    users = CustomUserSerializer(many=True, read_only=True, source='customUser_companyCode')  # sourceはCustomUserモデルのrelated_name
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'users']
