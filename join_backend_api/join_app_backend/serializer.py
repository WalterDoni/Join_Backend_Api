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
        fields = ['id', 'titleFromSub', 'status']
        
      
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['id', 'categoryColor', 'title', 'description', 'priority', 'category', 'subtask', 'author', 'assignedTo', 'section', 'date']