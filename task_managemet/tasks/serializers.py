from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


    def validate_status(self, value):
        if not value.isalpha():
            raise serializers.ValidationError('ტექსტი არ შეიძლება შეიცავდეს სიმბოლოებს')
        return value
