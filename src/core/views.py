from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from core.models import ToDo
from core.serializers import ToDoSerializer, UserSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    """This viewset automaitcally provides create, read, update, and delete actions."""

    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
