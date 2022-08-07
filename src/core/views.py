from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from core.models import ToDo
from core.serializers import ToDoSerializer, UserSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    """This viewset automaitcally provides create, read, update, and delete actions."""

    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
