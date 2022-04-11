from rest_framework import serializers
from core.models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):
    capacity = serializers.SerializerMethodField()
    consumption_per_min = serializers.SerializerMethodField()
    max_minutes_able_to_fly = serializers.SerializerMethodField()

    class Meta:
        model = Airplane
        fields = [
            'airplane_id',
            'airplane_name',
            'passengers_count',
            'capacity',
            'consumption_per_min',
            'max_minutes_able_to_fly'
        ]

    def get_capacity(self, obj: Airplane) -> str:
        return f"{obj.capacity} ℓ"

    def get_consumption_per_min(self, obj: Airplane) -> str:
        return f"{obj.fuel_consumption_per_min} ℓ/min"

    def get_max_minutes_able_to_fly(self, obj: Airplane) -> str:
        return f"{obj.max_minutes_able_to_fly} min"
