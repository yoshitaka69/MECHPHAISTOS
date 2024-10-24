from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, data):
        print("Data received for validation:", data)  # バリデーション前のデータをターミナルに出力
        return data

    def create(self, validated_data):
        print("Validated data received for creation:", validated_data)  # バリデーションを通過したデータをターミナルに出力
        instance = super().create(validated_data)
        print("Created instance:", instance)  # 作成されたインスタンスをターミナルに出力
        return instance

    def update(self, instance, validated_data):
        print("Validated data received for update:", validated_data)  # バリデーションを通過したデータをターミナルに出力
        instance = super().update(instance, validated_data)
        print("Updated instance:", instance)  # 更新されたインスタンスをターミナルに出力
        return instance



from rest_framework import serializers
from .models import GanttTest

class GanttTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GanttTest
        fields = ['id', 'name', 'start_date', 'end_date']



from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'start', 'end', 'background_color', 'border_color']