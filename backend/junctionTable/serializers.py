from rest_framework import serializers
from .models import MasterDataTable
from accounts.models import CompanyCode


class MasterDataTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = MasterDataTable #呼び出すモデル名
        fields = ['companyCode','companyName','plant','ceList_Id','equipment','machineName','taskCode','taskName','typeOfPM','laborCostOfPM','countOfPM','latestPM','periodOfPM','bomCode','maxPartsDeliveryTimeInBom','constructionPeriod','nextEventDate','situation','levelSetValue','mttr','possibilityOfProductionLv','impactForProduction','probabilityOfFailure','assessment','rcaOrReplace','sparePartsOrAlternative','coveredFromTask','twoways','ceDescription','thisYear10ago','thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago','thisYear','thisYear1later','thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later']# API上に表示するモデルのデータ項目


class CompanyCodeMDTSerializer(serializers.ModelSerializer):
    masterDataTableList = MasterDataTableSerializer(many=True, read_only=True, source='masterDataTable_companyCode')#ここのsourceは本当に注意
    
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'masterDataTableList']

