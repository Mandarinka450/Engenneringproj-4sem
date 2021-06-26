from rest_framework import serializers
from .models import Services


class ServicesSerializer(serializers.Serializer):
    id_service = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    tariff_plan = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    id_specialist = serializers.IntegerField()

    def create(self, validated_data):
        return Services.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_service = validated_data.get('id_service', instance.id_service)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.tariff_plan = validated_data.get('tariff_plan', instance.tariff_plan)
        instance.price = validated_data.get('price', instance.price)
        instance.id_specialist = validated_data.get('id_specialist', instance.id_specialist)

        instance.save()
        return instance
