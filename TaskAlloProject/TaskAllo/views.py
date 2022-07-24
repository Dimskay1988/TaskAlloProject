from rest_framework import viewsets, response
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend

class TaskViewSet(viewsets.ModelViewSet):
    """Список задач"""
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class TeamVievSet(viewsets.ModelViewSet):
    """Список комманд"""
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

class UsersVievSet(viewsets.ModelViewSet):
    """Список всех пользователей"""
    sserializer_class = EmployeeSerializer
    queryset = Employee.objects.all()