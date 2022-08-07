from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core import views

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'api/todolist', views.ToDoViewSet)
router.register(r'api/users', views.UserViewSet)

# The API urls are determined automatically by the router
# Include login urls for the browsable API
urlpatterns = [
    path(r'', include(router.urls)),
]
