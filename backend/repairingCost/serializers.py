
from rest_framework import serializers
from accounts.models import CompanyCode
from .models import PlannedPM02,ActualPM02,PlannedPM03,ActualPM03,ActualPM04,PlannedPM05,ActualPM05,CalTablePlannedPM02,CalTableActualPM02,CalTablePlannedPM03,CalTableActualPM03,CalTableActualPM04,CalTablePlannedPM05,CalTableActualPM05,SummedCost

from accounts.models import CompanyCode,Plant
from module.serializers import CommonSerializerMethodMixin
from accounts.serializers import PlantSerializer

import logging




class PlannedPM02Serializer(CommonSerializerMethodMixin,serializers.ModelSerializer):
    totalCost = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = PlannedPM02
        fields = ['companyCode','plant','year','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec','commitment','totalCost',]
        

    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode', 
        queryset=CompanyCode.objects.all()
    )
    plant = serializers.SlugRelatedField(
        slug_field='plant', 
        queryset=Plant.objects.all()
    )

    def update(self, instance, validated_data):
        # instanceのフィールドを更新
        instance = super().update(instance, validated_data)
        
        # totalCostを再計算して保存
        self.save_total_cost(instance)

        return instance


class PlantPPM02Serializer(serializers.ModelSerializer):
    plannedPM02 = PlannedPM02Serializer(many=True, source='plannedPM02_plant')  # Co2 モデルの related_name

    class Meta:
        model = Plant
        fields = ['plant', 'plannedPM02']


class CompanyCodePPM02Serializer(serializers.ModelSerializer):
    plannedPM02List = PlantPPM02Serializer(many=True, source='plant_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM02List']

    def update(self, instance, validated_data):
        plant_data_list = validated_data.pop('plant_companyCode', [])
        
        # CompanyCodeの基本フィールドを更新
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # PlantとPlannedPM02のデータを更新
        for plant_data in plant_data_list:
            planned_pm02_data = plant_data.pop('plannedPM02_plant', [])
            
            # Plantオブジェクトの取得または作成
            plant_instance, created = Plant.objects.get_or_create(
                companyCode=instance,
                plant=plant_data.get('plant'),
                defaults=plant_data
            )

            # 既存のPlantの場合、属性を更新
            if not created:
                for key, value in plant_data.items():
                    setattr(plant_instance, key, value)
                plant_instance.save()

            # PlannedPM02の処理
            for planned_pm02 in planned_pm02_data:
                planned_pm02_instance, created = PlannedPM02.objects.get_or_create(
                    plant=plant_instance, 
                    year=planned_pm02.get('year'),
                    defaults=planned_pm02
                )

                # PlannedPM02の更新または作成
                if not created:
                    for key, value in planned_pm02.items():
                        setattr(planned_pm02_instance, key, value)
                planned_pm02_instance.save()

        return instance

    def create(self, validated_data):
        # CompanyCodeに関連するPlantデータを抽出
        plant_data_list = validated_data.pop('plant_companyCode', [])

        # CompanyCodeインスタンスを取得または作成
        company_code_data = validated_data.pop('companyCode')
        company_code_instance, created = CompanyCode.objects.get_or_create(
            companyCode=company_code_data, 
            defaults=validated_data
        )

        # 既存のCompanyCodeの場合、更新
        if not created:
            for attr, value in validated_data.items():
                setattr(company_code_instance, attr, value)
            company_code_instance.save()

        # PlantとPlannedPM02のデータの処理
        for plant_data in plant_data_list:
            planned_pm02_data = plant_data.pop('plannedPM02_plant', [])
            plant_instance, created = Plant.objects.get_or_create(
                companyCode=company_code_instance, 
                plant=plant_data.get('plant'),
                defaults=plant_data
            )

            # 既存のPlantの場合、属性を更新
            if not created:
                for key, value in plant_data.items():
                    setattr(plant_instance, key, value)
                plant_instance.save()

            # PlannedPM02の処理
            for planned_pm02 in planned_pm02_data:
                planned_pm02_instance, created = PlannedPM02.objects.get_or_create(
                    plant=plant_instance, 
                    year=planned_pm02.get('year'),
                    defaults=planned_pm02
                )

                # PlannedPM02の更新または作成
                if not created:
                    for key, value in planned_pm02.items():
                        setattr(planned_pm02_instance, key, value)
                planned_pm02_instance.save()

        return company_code_instance


    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM02List']









#Actual PM02 cost
class ActualPM02Serializer(CommonSerializerMethodMixin,serializers.ModelSerializer):
    totalCost = serializers.SerializerMethodField

    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode', 
        queryset=CompanyCode.objects.all()
    )
    plant = serializers.SlugRelatedField(
        slug_field='plant', 
        queryset=Plant.objects.all()
    )

    def update(self, instance, validated_data):
        # instanceのフィールドを更新
        instance = super().update(instance, validated_data)
        
        # totalCostを再計算して保存
        self.save_total_cost(instance)

        return instance
    
    class Meta:
        model = ActualPM02
        fields = ['companyCode','plant','year','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec','commitment','totalCost',]

class PlantAPM02Serializer(serializers.ModelSerializer):
    actualPM02 = ActualPM02Serializer(many=True, source='actualPM02_plant')  # Co2 モデルの related_name

    class Meta:
        model = Plant
        fields = ['plant', 'actualPM02']
    

class CompanyCodeAPM02Serializer(serializers.ModelSerializer):
    actualPM02List = PlantAPM02Serializer(many=True, source='plant_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM02List']

    def update(self, instance, validated_data):
        plant_data_list = validated_data.pop('plant_companyCode', [])
        
        # CompanyCodeの基本フィールドを更新
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # PlantとActualPM02のデータを更新
        for plant_data in plant_data_list:
            actual_pm02_data = plant_data.pop('actualPM02_plant', [])
            
            # Plantオブジェクトの取得または作成
            plant_instance, created = Plant.objects.get_or_create(
                companyCode=instance,
                plant=plant_data.get('plant'),
                defaults=plant_data
            )

            # 既存のPlantの場合、属性を更新
            if not created:
                for key, value in plant_data.items():
                    setattr(plant_instance, key, value)
                plant_instance.save()

            # ActualPM02の処理
            for actual_pm02 in actual_pm02_data:
                actual_pm02_instance, created = ActualPM02.objects.get_or_create(
                    plant=plant_instance, 
                    year=actual_pm02.get('year'),
                    defaults=actual_pm02
                )

                # ActualPM02の更新または作成
                if not created:
                    for key, value in actual_pm02.items():
                        setattr(actual_pm02_instance, key, value)
                actual_pm02_instance.save()

                # totalCostの更新
                actual_pm02_serializer = ActualPM02Serializer()
                actual_pm02_serializer.save_total_cost(actual_pm02_instance)

        return instance

    def create(self, validated_data):
        # CompanyCodeに関連するPlantデータを抽出
        plant_data_list = validated_data.pop('plant_companyCode', [])

        # CompanyCodeインスタンスを取得または作成
        company_code_data = validated_data.pop('companyCode')
        company_code_instance, created = CompanyCode.objects.get_or_create(
            companyCode=company_code_data, 
            defaults=validated_data
        )

        # 既存のCompanyCodeの場合、更新
        if not created:
            for attr, value in validated_data.items():
                setattr(company_code_instance, attr, value)
            company_code_instance.save()

        # PlantとActualPM02のデータの処理
        for plant_data in plant_data_list:
            actual_pm02_data = plant_data.pop('actualPM02_plant', [])
            plant_instance, created = Plant.objects.get_or_create(
                companyCode=company_code_instance, 
                plant=plant_data.get('plant'),
                defaults=plant_data
            )

            # 既存のPlantの場合、属性を更新
            if not created:
                for key, value in plant_data.items():
                    setattr(plant_instance, key, value)
                plant_instance.save()

            # ActualPM02の処理
            for actual_pm02 in actual_pm02_data:
                actual_pm02_instance, created = ActualPM02.objects.get_or_create(
                    plant=plant_instance, 
                    year=actual_pm02.get('year'),
                    defaults=actual_pm02
                )

                # ActualPM02の更新または作成
                if not created:
                    for key, value in actual_pm02.items():
                        setattr(actual_pm02_instance, key, value)
                actual_pm02_instance.save()

                # totalCostの更新
                actual_pm02_serializer = ActualPM02Serializer()
                actual_pm02_serializer.save_total_cost(actual_pm02_instance)

        return company_code_instance
    

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM02List']












#plannedPM03
class PlannedPM03Serializer(CommonSerializerMethodMixin,serializers.ModelSerializer):
    totalCost = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = PlannedPM03
        fields = ['companyCode','plant','year','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec','commitment','totalCost',]
        
    # createとupdateメソッドで共通ロジックを呼び出す
    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode', 
        queryset=CompanyCode.objects.all()
    )
    plant = serializers.SlugRelatedField(
        slug_field='plant', 
        queryset=Plant.objects.all()
    )

    def update(self, instance, validated_data):
        # instanceのフィールドを更新
        instance = super().update(instance, validated_data)
        
        # totalCostを再計算して保存
        self.save_total_cost(instance)

        return instance

class PlantPPM03Serializer(serializers.ModelSerializer):
    plannedPM03 = PlannedPM03Serializer(many=True, source='plannedPM03_plant') 

    class Meta:
        model = Plant
        fields = ['plant', 'plannedPM03']


class CompanyCodePPM03Serializer(serializers.ModelSerializer):
    plannedPM03List = PlantPPM03Serializer(many=True, source='plant_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM03List']


    def update(self, instance, validated_data):
        plant_data_list = validated_data.pop('plant_companyCode', [])
        
        for plant_data in plant_data_list:
            planned_pm03_data = plant_data.pop('plannedPM03_plant', [])
            plant_instance, created = Plant.objects.get_or_create(
                companyCode=instance,
                plant=plant_data.get('plant'),
                defaults=plant_data
            )

            if not created:
                for key, value in plant_data.items():
                    setattr(plant_instance, key, value)
                plant_instance.save()

            for planned_pm03 in planned_pm03_data:
                planned_pm03_instance, created = PlannedPM03.objects.get_or_create(
                    plant=plant_instance, 
                    year=planned_pm03.get('year'),
                    defaults=planned_pm03
                )

                if not created:
                    for key, value in planned_pm03.items():
                        setattr(planned_pm03_instance, key, value)
                    planned_pm03_instance.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

    def create(self, validated_data):
        plant_data_list = validated_data.pop('plant_companyCode', [])
        company_code_data = validated_data.pop('companyCode')
        company_code_instance, created = CompanyCode.objects.get_or_create(
            companyCode=company_code_data, 
            defaults=validated_data
        )

        if not created:
            for attr, value in validated_data.items():
                setattr(company_code_instance, attr, value)
            company_code_instance.save()

        for plant_data in plant_data_list:
            planned_pm03_data = plant_data.pop('plannedPM03_plant', [])
            plant_instance, created = Plant.objects.get_or_create(
                companyCode=company_code_instance, 
                plant=plant_data.get('plant'),
                defaults=plant_data
            )

            if not created:
                for key, value in plant_data.items():
                    setattr(plant_instance, key, value)
                plant_instance.save()

            for planned_pm03 in planned_pm03_data:
                planned_pm03_instance, created = PlannedPM03.objects.get_or_create(
                    plant=plant_instance, 
                    year=planned_pm03.get('year'),
                    defaults=planned_pm03
                )

                if not created:
                    for key, value in planned_pm03.items():
                        setattr(planned_pm03_instance, key, value)
                    planned_pm03_instance.save()

        return company_code_instance


    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM03List']










#PM03actual

class ActualPM03Serializer(serializers.ModelSerializer):

    class Meta:
        model = ActualPM03
        fields = ['companyCode','plant','year','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec','commitment','totalCost',]


    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode', 
        queryset=CompanyCode.objects.all()
    )
    plant = serializers.SlugRelatedField(
        slug_field='plant', 
        queryset=Plant.objects.all()
    )


class PlantAPM03Serializer(serializers.ModelSerializer):
    actualPM03 = ActualPM03Serializer(many=True, source='actualPM03_plant')  

    class Meta:
        model = Plant
        fields = ['plant', 'actualPM03']
    

class CompanyCodeAPM03Serializer(serializers.ModelSerializer):
    actualPM03List = PlantAPM03Serializer(many=True, source='plant_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM03List']

    def update(self, instance, validated_data):
        plant_data_list = validated_data.pop('plant_companyCode', [])
        for plant_data in plant_data_list:
            actual_pm03_data = plant_data.pop('actualPM03_plant', [])
            plant_instance, created = Plant.objects.get_or_create(
                companyCode=instance,
                plant=plant_data.get('plant'),
                defaults=plant_data
            )

            if not created:
                for key, value in plant_data.items():
                    setattr(plant_instance, key, value)
                plant_instance.save()

            for actual_pm03 in actual_pm03_data:
                actual_pm03_instance, created = ActualPM03.objects.get_or_create(
                    plant=plant_instance, 
                    year=actual_pm03.get('year'),
                    defaults=actual_pm03
                )

                if not created:
                    for key, value in actual_pm03.items():
                        setattr(actual_pm03_instance, key, value)
                    actual_pm03_instance.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

    def create(self, validated_data):
        plant_data_list = validated_data.pop('plant_companyCode', [])
        company_code_data = validated_data.pop('companyCode')
        company_code_instance, created = CompanyCode.objects.get_or_create(
            companyCode=company_code_data, 
            defaults=validated_data
        )

        if not created:
            for attr, value in validated_data.items():
                setattr(company_code_instance, attr, value)
            company_code_instance.save()

        for plant_data in plant_data_list:
            actual_pm03_data = plant_data.pop('actualPM03_plant', [])
            plant_instance, created = Plant.objects.get_or_create(
                companyCode=company_code_instance, 
                plant=plant_data.get('plant'),
                defaults=plant_data
            )

            if not created:
                for key, value in plant_data.items():
                    setattr(plant_instance, key, value)
                plant_instance.save()

            for actual_pm03 in actual_pm03_data:
                actual_pm03_instance, created = ActualPM03.objects.get_or_create(
                    plant=plant_instance, 
                    year=actual_pm03.get('year'),
                    defaults=actual_pm03
                )

                if not created:
                    for key, value in actual_pm03.items():
                        setattr(actual_pm03_instance, key, value)
                    actual_pm03_instance.save()

        return company_code_instance













#PM04-actual
class ActualPM04Serializer(serializers.ModelSerializer):
    class Meta:
        model = ActualPM04
        fields = ['companyCode','plant','year','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec','commitment','totalCost',]


    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode', 
        queryset=CompanyCode.objects.all()
    )
    plant = serializers.SlugRelatedField(
        slug_field='plant', 
        queryset=Plant.objects.all()
    )

    

class PlantAPM04Serializer(serializers.ModelSerializer):
    actualPM04 = ActualPM04Serializer(many=True, source='actualPM04_plant') 

    class Meta:
        model = Plant
        fields = ['plant', 'actualPM04']
    

class CompanyCodeAPM04Serializer(serializers.ModelSerializer):
    actualPM04List = PlantAPM04Serializer(many=True, source='plant_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM04List']

    def update(self, instance, validated_data):
        plant_data_list = validated_data.pop('plant_companyCode', [])
        
        for plant_data in plant_data_list:
            actual_pm04_data = plant_data.pop('actualPM04_plant', [])
            plant_instance, created = Plant.objects.get_or_create(
                companyCode=instance,
                plant=plant_data.get('plant'),
                defaults=plant_data
            )

            if not created:
                for key, value in plant_data.items():
                    setattr(plant_instance, key, value)
                plant_instance.save()

            for actual_pm04 in actual_pm04_data:
                actual_pm04_instance, created = ActualPM04.objects.get_or_create(
                    plant=plant_instance, 
                    year=actual_pm04.get('year'),
                    defaults=actual_pm04
                )

                if not created:
                    for key, value in actual_pm04.items():
                        setattr(actual_pm04_instance, key, value)
                    actual_pm04_instance.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

    def create(self, validated_data):
        plant_data_list = validated_data.pop('plant_companyCode', [])
        company_code_data = validated_data.pop('companyCode')
        company_code_instance, created = CompanyCode.objects.get_or_create(
            companyCode=company_code_data, 
            defaults=validated_data
        )

        if not created:
            for attr, value in validated_data.items():
                setattr(company_code_instance, attr, value)
            company_code_instance.save()

        for plant_data in plant_data_list:
            actual_pm04_data = plant_data.pop('actualPM04_plant', [])
            plant_instance, created = Plant.objects.get_or_create(
                companyCode=company_code_instance, 
                plant=plant_data.get('plant'),
                defaults=plant_data
            )

            if not created:
                for key, value in plant_data.items():
                    setattr(plant_instance, key, value)
                plant_instance.save()

            for actual_pm04 in actual_pm04_data:
                actual_pm04_instance, created = ActualPM04.objects.get_or_create(
                    plant=plant_instance, 
                    year=actual_pm04.get('year'),
                    defaults=actual_pm04
                )

                if not created:
                    for key, value in actual_pm04.items():
                        setattr(actual_pm04_instance, key, value)
                    actual_pm04_instance.save()

        return company_code_instance


    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM04List']







class PlannedPM05Serializer(serializers.ModelSerializer):
    class Meta:
        model = PlannedPM05
        fields = ['companyCode','plant','year','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec','commitment','totalCost',]
        
    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode', 
        queryset=CompanyCode.objects.all()
    )
    plant = serializers.SlugRelatedField(
        slug_field='plant', 
        queryset=Plant.objects.all()
    )


class PlantPPM05Serializer(serializers.ModelSerializer):
    plannedPM05 = PlannedPM05Serializer(many=True, source='plannedPM05_plant') 

    class Meta:
        model = Plant
        fields = ['plant', 'plannedPM05']


class CompanyCodePPM05Serializer(serializers.ModelSerializer):
    plannedPM05List = PlantPPM05Serializer(many=True, source='plant_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM05List']

    def update(self, instance, validated_data):
        plant_data_list = validated_data.pop('plant_companyCode', [])
        
        for plant_data in plant_data_list:
            planned_pm05_data = plant_data.pop('plannedPM05_plant', [])
            plant_instance, created = Plant.objects.get_or_create(
                companyCode=instance,
                plant=plant_data.get('plant'),
                defaults=plant_data
            )

            if not created:
                for key, value in plant_data.items():
                    setattr(plant_instance, key, value)
                plant_instance.save()

            for planned_pm05 in planned_pm05_data:
                planned_pm05_instance, created = PlannedPM05.objects.get_or_create(
                    plant=plant_instance, 
                    year=planned_pm05.get('year'),
                    defaults=planned_pm05
                )

                if not created:
                    for key, value in planned_pm05.items():
                        setattr(planned_pm05_instance, key, value)
                    planned_pm05_instance.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

    def create(self, validated_data):
        plant_data_list = validated_data.pop('plant_companyCode', [])
        company_code_data = validated_data.pop('companyCode')
        company_code_instance, created = CompanyCode.objects.get_or_create(
            companyCode=company_code_data, 
            defaults=validated_data
        )

        if not created:
            for attr, value in validated_data.items():
                setattr(company_code_instance, attr, value)
            company_code_instance.save()

        for plant_data in plant_data_list:
            planned_pm05_data = plant_data.pop('plannedPM05_plant', [])
            plant_instance, created = Plant.objects.get_or_create(
                companyCode=company_code_instance, 
                plant=plant_data.get('plant'),
                defaults=plant_data
            )

            if not created:
                for key, value in plant_data.items():
                    setattr(plant_instance, key, value)
                plant_instance.save()

            for planned_pm05 in planned_pm05_data:
                planned_pm05_instance, created = PlannedPM05.objects.get_or_create(
                    plant=plant_instance, 
                    year=planned_pm05.get('year'),
                    defaults=planned_pm05
                )

                if not created:
                    for key, value in planned_pm05.items():
                        setattr(planned_pm05_instance, key, value)
                    planned_pm05_instance.save()

        return company_code_instance


    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM05List']






#PM05^actual
class ActualPM05Serializer(serializers.ModelSerializer):
    class Meta:
        model = ActualPM05
        fields = ['companyCode','plant','year','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec','commitment','totalCost',]


    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode', 
        queryset=CompanyCode.objects.all()
    )
    plant = serializers.SlugRelatedField(
        slug_field='plant', 
        queryset=Plant.objects.all()
    )


class PlantAPM05Serializer(serializers.ModelSerializer):
    actualPM05 = ActualPM05Serializer(many=True, source='actualPM05_plant')  # Co2 モデルの related_name

    class Meta:
        model = Plant
        fields = ['plant', 'actualPM05']
    

class CompanyCodeAPM05Serializer(serializers.ModelSerializer):
    actualPM05List = PlantAPM05Serializer(many=True, source='plant_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM05List']

    def update(self, instance, validated_data):
        plant_data_list = validated_data.pop('plant_companyCode', [])
        
        for plant_data in plant_data_list:
            actual_pm05_data = plant_data.pop('actualPM05_plant', [])
            plant_instance, created = Plant.objects.get_or_create(
                companyCode=instance,
                plant=plant_data.get('plant'),
                defaults=plant_data
            )

            if not created:
                for key, value in plant_data.items():
                    setattr(plant_instance, key, value)
                plant_instance.save()

            for actual_pm05 in actual_pm05_data:
                actual_pm05_instance, created = ActualPM05.objects.get_or_create(
                    plant=plant_instance, 
                    year=actual_pm05.get('year'),
                    defaults=actual_pm05
                )

                if not created:
                    for key, value in actual_pm05.items():
                        setattr(actual_pm05_instance, key, value)
                    actual_pm05_instance.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

    def create(self, validated_data):
        plant_data_list = validated_data.pop('plant_companyCode', [])
        company_code_data = validated_data.pop('companyCode')
        company_code_instance, created = CompanyCode.objects.get_or_create(
            companyCode=company_code_data, 
            defaults=validated_data
        )

        if not created:
            for attr, value in validated_data.items():
                setattr(company_code_instance, attr, value)
            company_code_instance.save()

        for plant_data in plant_data_list:
            actual_pm05_data = plant_data.pop('actualPM05_plant', [])
            plant_instance, created = Plant.objects.get_or_create(
                companyCode=company_code_instance, 
                plant=plant_data.get('plant'),
                defaults=plant_data
            )

            if not created:
                for key, value in plant_data.items():
                    setattr(plant_instance, key, value)
                plant_instance.save()

            for actual_pm05 in actual_pm05_data:
                actual_pm05_instance, created = ActualPM05.objects.get_or_create(
                    plant=plant_instance, 
                    year=actual_pm05.get('year'),
                    defaults=actual_pm05
                )

                if not created:
                    for key, value in actual_pm05.items():
                        setattr(actual_pm05_instance, key, value)
                    actual_pm05_instance.save()

        return company_code_instance


    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM05List']







#ここからCalTable
#PM02
class CalTablePPM02Serializer(serializers.ModelSerializer):
    no1RepairingCost = serializers.SerializerMethodField()
    no2RepairingCost = serializers.SerializerMethodField()
    no3RepairingCost = serializers.SerializerMethodField()
    no4RepairingCost = serializers.SerializerMethodField()
    no5RepairingCost = serializers.SerializerMethodField()
    
    class Meta:
        model = CalTablePlannedPM02
        fields =  ['companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost']


        
class CompanyCodeCalPPM02Serializer(serializers.ModelSerializer):
    calPPM02List = CalTablePPM02Serializer(many=True, read_only=True, source='calTablePlanPM02_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calPPM02List']



class CalTableAPM02Serializer(serializers.ModelSerializer):
    no1RepairingCost = serializers.SerializerMethodField()
    no2RepairingCost = serializers.SerializerMethodField()
    no3RepairingCost = serializers.SerializerMethodField()
    no4RepairingCost = serializers.SerializerMethodField()
    no5RepairingCost = serializers.SerializerMethodField()
    
    class Meta:
        model = CalTableActualPM02
        fields =  ['companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost']




class CompanyCodeCalAPM02Serializer(serializers.ModelSerializer):
    calAPM02List = CalTableAPM02Serializer(many=True, read_only=True, source='calTableActualPM02_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calAPM02List']




#PM03
class CalTablePPM03Serializer(serializers.ModelSerializer):
    no1RepairingCost = serializers.SerializerMethodField()
    no2RepairingCost = serializers.SerializerMethodField()
    no3RepairingCost = serializers.SerializerMethodField()
    no4RepairingCost = serializers.SerializerMethodField()
    no5RepairingCost = serializers.SerializerMethodField()
    
    class Meta:
        model = CalTablePlannedPM03
        fields =  ['companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost']


        
        
class CompanyCodeCalPPM03Serializer(serializers.ModelSerializer):
    calPPM03List = CalTablePPM03Serializer(many=True, read_only=True, source='calTablePlanPM03_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calPPM03List']





class CalTableAPM03Serializer(serializers.ModelSerializer):
    no1RepairingCost = serializers.SerializerMethodField()
    no2RepairingCost = serializers.SerializerMethodField()
    no3RepairingCost = serializers.SerializerMethodField()
    no4RepairingCost = serializers.SerializerMethodField()
    no5RepairingCost = serializers.SerializerMethodField()

    class Meta:
        model = CalTableActualPM03
        fields =  ['companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost']


        
class CompanyCodeCalAPM03Serializer(serializers.ModelSerializer):
    calAPM03List = CalTableAPM03Serializer(many=True, read_only=True, source='calTableActualPM03_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calAPM03List']




#PM04
class CalTableAPM04Serializer(serializers.ModelSerializer):
    no1RepairingCost = serializers.SerializerMethodField()
    no2RepairingCost = serializers.SerializerMethodField()
    no3RepairingCost = serializers.SerializerMethodField()
    no4RepairingCost = serializers.SerializerMethodField()
    no5RepairingCost = serializers.SerializerMethodField()
    
    class Meta:
        model = CalTableActualPM04
        fields =  ['companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost']


        
class CompanyCodeCalPPM04Serializer(serializers.ModelSerializer):
    calPPM04List = CalTableAPM04Serializer(many=True, read_only=True, source='calTablePlanPM04_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calPPM04List']




class CalTablePPM05Serializer(serializers.ModelSerializer):
    no1RepairingCost = serializers.SerializerMethodField()
    no2RepairingCost = serializers.SerializerMethodField()
    no3RepairingCost = serializers.SerializerMethodField()
    no4RepairingCost = serializers.SerializerMethodField()
    no5RepairingCost = serializers.SerializerMethodField()
    
    class Meta:
        model = CalTablePlannedPM05
        fields = ['companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost']


class CompanyCodeCalPPM05Serializer(serializers.ModelSerializer):
    calPPM05List = CalTablePPM05Serializer(many=True, read_only=True, source='calTablePlannedPM05_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calPPM05List']





class CalTableAPM05Serializer(serializers.ModelSerializer):
    no1RepairingCost = serializers.SerializerMethodField()
    no2RepairingCost = serializers.SerializerMethodField()
    no3RepairingCost = serializers.SerializerMethodField()
    no4RepairingCost = serializers.SerializerMethodField()
    no5RepairingCost = serializers.SerializerMethodField()
    
    class Meta:
        model = CalTableActualPM05
        fields = ['companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost']


class CompanyCodeCalAPM05Serializer(serializers.ModelSerializer):
    calAPM05List = CalTableAPM05Serializer(many=True, read_only=True, source='calTableActualPM05_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calAPM05List']





class SummedCostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SummedCost
        fields = ['year','sumJan','sumFeb','sumMar','sumApr','sumMay','sumJun','sumJul','sumAug','sumSep','sumOct','sumNov','sumDec','sumCommitment','totalActualPM02','totalActualPM03','totalActuamPM04','totalActualPM05','totalActualCost']

class CompanyCodeSummedCostSerializer(serializers.ModelSerializer):
    summedCostList = SummedCostSerializer(many=True, read_only=True, source='summedCost_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'summedCostList']
