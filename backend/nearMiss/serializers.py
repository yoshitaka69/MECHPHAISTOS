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

    userに対するForeignKeyのfillter機能
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            # 特定の masterCode を持つユーザーの場合、すべてのレコードを表示
            if user.companyCode.masterCode == 'MASTER123':
                return MyModel.objects.all()
            # それ以外のユーザーにはその companyCode に関連するレコードのみを表示
            else:
                return MyModel.objects.filter(companyCode=user.companyCode)
        else:
            # 認証されていないユーザーには空のクエリセットを返す
            return MyModel.objects.none()
    
    def create(self, validated_data):
    # companyName から値を取得
    company_name = validated_data.get('companyName', '')
    if company_name:
        # companyName に基づいて連番を生成
        last_near_miss = NearMiss.objects.filter(nearMissNo__startswith=company_name).order_by('-nearMissNo').first()

        if last_near_miss:
            # companyName で切り出した後の数字の部分を取得
            try:
                last_number_str = last_near_miss.nearMissNo.split(company_name + '-')[1]
                last_number = int(last_number_str)
                new_code_number = last_number + 1
            except (IndexError, ValueError):
                new_code_number = 1
        else:
            new_code_number = 1

        validated_data['nearMissNo'] = f'{company_name}-{str(new_code_number).zfill(3)}'
    else:
        # companyName が提供されていない場合、デフォルトの連番を使用
        validated_data['nearMissNo'] = 'default-001'

    return NearMiss.objects.create(**validated_data)


class CompanyNearMissSerializer(serializers.ModelSerializer):
    nearMissList = NearMissSerializer(many=True, read_only=True, source='nearMiss_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'nearMissList']
