from rest_framework import serializers
from .models import NearMiss, CompanyCode

class NearMissSerializer(serializers.ModelSerializer):
    nearMissNo = serializers.CharField(read_only=True)
    dateOfOccurrence = serializers.DateField(format="%Y-%m-%d")
    createdDay = serializers.DateTimeField(format="%Y-%m-%d",read_only=True)
    updateDay = serializers.DateTimeField(format="%Y-%m-%d",read_only=True)
    safetyIndicater = serializers.CharField(read_only=True)

    class Meta:
        model = NearMiss
        fields = ['id','companyCode','companyName','nearMissNo','userName','department','dateOfOccurrence','placeOfOccurrence','typeOfAccident','factor','injuredLv','equipmentDamageLv','affectOfEnviroment','newsCoverage','measures','safetyIndicater','description','createdDay','updateDay',]
        #fields = '__all__'
    
    def create(self, validated_data):
        # CompanyCode オブジェクトから文字列の値を取得
        company_code_obj = validated_data.get('companyCode')
        if company_code_obj:
            company_code_str = str(company_code_obj)  # ここでオブジェクトを文字列に変換
        else:
            company_code_str = ''

        last_near_miss = NearMiss.objects.filter(nearMissNo__startswith=company_code_str).order_by('-nearMissNo').first()

        if last_near_miss:
            # company_code_str の長さに応じて last_near_miss.nearMissNo から数値部分を取り出し
            last_number = int(last_near_miss.nearMissNo[len(company_code_str):])
            new_code_number = last_number + 1
        else:
            new_code_number = 1

        validated_data['nearMissNo'] = f'{company_code_str}{str(new_code_number).zfill(3)}'
        return NearMiss.objects.create(**validated_data)

class CompanyNearMissSerializer(serializers.ModelSerializer):
    nearMissList = NearMissSerializer(many=True, read_only=True, source='nearMiss_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'nearMissList']
