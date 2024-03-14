from rest_framework import serializers

from module.utils import calculate_total_cost



class CommonSerializerMethodMixin:
    totalCost = serializers.SerializerMethodField(read_only=True)

    def get_totalCost(self, obj):
        return calculate_total_cost(obj)

    def save_total_cost(self, instance):
        instance.totalCost = self.get_totalCost(instance)
        instance.save()
