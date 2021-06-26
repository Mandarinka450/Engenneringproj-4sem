from rest_framework import serializers
from .models import Articles

class ArticlesSerializer(serializers.Serializer):
    id_articles = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=55)
    description = serializers.CharField()


    def create(self, validated_data):
        return Articles.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.id_articles = validated_data.get('id_articles', instance.id_articles)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
