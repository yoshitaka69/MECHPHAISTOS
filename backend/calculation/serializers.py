
from rest_framework import serializers
from accounts.models import CompanyCode,Plant
from .models import (CalTablePlannedPM02,CalTableActualPM02,
                     CalTablePlannedPM03,CalTableActualPM03,
                     CalTableActualPM04,
                     CalTablePlannedPM05,CalTableActualPM05,
                     SummedPlannedCost,
                     SummedActualCost)



#CalTablePPM02
class CalTablePPM02Serializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
    slug_field='companyCode', 
    queryset=CompanyCode.objects.all()
    )

    plant = serializers.SlugRelatedField(
    slug_field='plant', 
    queryset=Plant.objects.all()
)

    
    class Meta:
        model = CalTablePlannedPM02
        fields =  ['companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost']


        
class CompanyCodeCalPPM02Serializer(serializers.ModelSerializer):
    calPPM02List = CalTablePPM02Serializer(many=True, read_only=True, source='calTablePlanPM02_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calPPM02List']




#CalTableAPM02
class CalTableAPM02Serializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
    slug_field='companyCode', 
    queryset=CompanyCode.objects.all()
    )

    plant = serializers.SlugRelatedField(
    slug_field='plant', 
    queryset=Plant.objects.all()
)
 
    
    class Meta:
        model = CalTableActualPM02
        fields =  ['companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost']




class CompanyCodeCalAPM02Serializer(serializers.ModelSerializer):
    calAPM02List = CalTableAPM02Serializer(many=True, read_only=True, source='calTableActualPM02_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calAPM02List']




#CalTablePPM03
class CalTablePPM03Serializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
    slug_field='companyCode', 
    queryset=CompanyCode.objects.all()
    )

    plant = serializers.SlugRelatedField(
    slug_field='plant', 
    queryset=Plant.objects.all()
)

    class Meta:
        model = CalTablePlannedPM03
        fields =  ['companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost']


        
        
class CompanyCodeCalPPM03Serializer(serializers.ModelSerializer):
    calPPM03List = CalTablePPM03Serializer(many=True, read_only=True, source='calTablePlanPM03_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calPPM03List']




#CalTableAPM03
class CalTableAPM03Serializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
    slug_field='companyCode', 
    queryset=CompanyCode.objects.all()
    )

    plant = serializers.SlugRelatedField(
    slug_field='plant', 
    queryset=Plant.objects.all()
)


    class Meta:
        model = CalTableActualPM03
        fields =  ['companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost']


        
class CompanyCodeCalAPM03Serializer(serializers.ModelSerializer):
    calAPM03List = CalTableAPM03Serializer(many=True, read_only=True, source='calTableActualPM03_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calAPM03List']




#CalTableAPM04
class CalTableAPM04Serializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
    slug_field='companyCode', 
    queryset=CompanyCode.objects.all()
    )

    plant = serializers.SlugRelatedField(
    slug_field='plant', 
    queryset=Plant.objects.all()
)
 
    
    class Meta:
        model = CalTableActualPM04
        fields =  ['companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost']


        
class CompanyCodeCalAPM04Serializer(serializers.ModelSerializer):
    calPPM04List = CalTableAPM04Serializer(many=True, read_only=True, source='calTablePlanPM04_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calPPM04List']



#CalTablePPM05
class CalTablePPM05Serializer(serializers.ModelSerializer):
  
    companyCode = serializers.SlugRelatedField(
    slug_field='companyCode', 
    queryset=CompanyCode.objects.all()
    )

    plant = serializers.SlugRelatedField(
    slug_field='plant', 
    queryset=Plant.objects.all()
)

    class Meta:
        model = CalTablePlannedPM05
        fields = ['companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost']


class CompanyCodeCalPPM05Serializer(serializers.ModelSerializer):
    calPPM05List = CalTablePPM05Serializer(many=True, read_only=True, source='calTablePlannedPM05_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calPPM05List']




#CalTableAPM05
class CalTableAPM05Serializer(serializers.ModelSerializer):
  
    companyCode = serializers.SlugRelatedField(
    slug_field='companyCode', 
    queryset=CompanyCode.objects.all()
    )

    plant = serializers.SlugRelatedField(
    slug_field='plant', 
    queryset=Plant.objects.all()
)
    
    class Meta:
        model = CalTableActualPM05
        fields = ['companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost']


class CompanyCodeCalAPM05Serializer(serializers.ModelSerializer):
    calAPM05List = CalTableAPM05Serializer(many=True, read_only=True, source='calTableActualPM05_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calAPM05List']




#SummedPlannedCost
class SummedPlannedCostSerializer(serializers.ModelSerializer):
    
    companyCode = serializers.SlugRelatedField(
    slug_field='companyCode', 
    queryset=CompanyCode.objects.all()
    )

    plant = serializers.SlugRelatedField(
    slug_field='plant', 
    queryset=Plant.objects.all()
)

    class Meta:
        model = SummedPlannedCost
        fields = ['companyCode','plant','year','sumJan','sumFeb','sumMar','sumApr','sumMay','sumJun','sumJul','sumAug','sumSep','sumOct','sumNov','sumDec','sumCommitment','totalPlannedPM02','totalPlannedPM03','totalPlannedPM04','totalPlannedPM05','totalPlannedCost']



class CompanyCodeSummedPlannedCostSerializer(serializers.ModelSerializer):
    summedPlannedCostList = SummedPlannedCostSerializer(many=True, read_only=True, source='summedPlannedCost_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'summedPlannedCostList']






#SummedActualCost
class SummedActualCostSerializer(serializers.ModelSerializer):
    
    companyCode = serializers.SlugRelatedField(
    slug_field='companyCode', 
    queryset=CompanyCode.objects.all()
    )

    plant = serializers.SlugRelatedField(
    slug_field='plant', 
    queryset=Plant.objects.all()
)

    class Meta:
        model = SummedActualCost
        fields = ['companyCode','plant','year','sumJan','sumFeb','sumMar','sumApr','sumMay','sumJun','sumJul','sumAug','sumSep','sumOct','sumNov','sumDec','sumCommitment','totalActualPM02','totalActualPM03','totalActualPM04','totalActualPM05','totalActualCost']



class CompanyCodeSummedActualCostSerializer(serializers.ModelSerializer):
    summedActualCostList = SummedActualCostSerializer(many=True, read_only=True, source='summedActualCost_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'summedActualCostList']
