from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from core.models import ToDo
from core.serializers import ToDoSerializer, UserSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    """This viewset automatcally provides create, read, update, and delete actions."""

    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """This viewset automatically provides read actions."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
