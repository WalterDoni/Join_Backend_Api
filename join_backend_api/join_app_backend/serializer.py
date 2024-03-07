from django.contrib.auth.models import User
from rest_framework import serializers
from .models import  *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ['id', 'name', 'email', 'phonenumber', 'short', 'iconColor', 'author']


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubtaskModel
        fields = '__all__'
        
class ColorSerialzier(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        fields = '__all__'
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['id', 'color', 'title', 'description', 'assigned_to', 'priority', 'category', 'subtask', 'author']