from dataclasses import field
from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import ToDo


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ToDo
        fields = ['url', 'id', 'owner', 'title', 'completed']
