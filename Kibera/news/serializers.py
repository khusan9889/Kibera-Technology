from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()
    author = serializers.CharField()
    created_date = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.body = validated_data.get("body", instance.body)
        instance.author = validated_data.get("author", instance.author)
        instance.created_date = validated_data.get("created_date", instance.created_date)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance