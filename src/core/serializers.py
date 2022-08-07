from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import ToDo


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ToDo
        fields = ['url', 'id', 'owner', 'title', 'completed']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    todo = serializers.HyperlinkedRelatedField(many=True, view_name='todo-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'todo']
