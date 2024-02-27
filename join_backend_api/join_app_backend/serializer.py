from django.contrib.auth.models import Group, User
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