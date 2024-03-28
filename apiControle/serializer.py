from rest_framework import serializers
from models import Classroom, Schedule

class ClassroomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    capacity = serializers.IntegerField()

    def create(self, validated_data):
        return Classroom(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        return instance

class ScheduleSerializer(serializers.Serializer):
    class_id = serializers.IntegerField()
    hour = serializers.TimeField()
    reserved = serializers.BooleanField()

    def create(self, validated_data):
        return Schedule(**validated_data)

    def update(self, instance, validated_data):
        instance.class_id = validated_data.get('class_id', instance.class_id)
        instance.hour = validated_data.get('hour', instance.hour)
        instance.reserved = validated_data.get('reserved', instance.reserved)
        return instance
