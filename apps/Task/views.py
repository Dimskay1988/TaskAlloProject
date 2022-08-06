from rest_framework import viewsets, response
from .serializers import TaskSerializer, ImageTaskSerializer
from .models import Task, ImageTask
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(viewsets.ModelViewSet):
    """Список задач"""
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]


class ImageTaskViewSet(viewsets.ModelViewSet):
    """Список изображений заданий"""
    serializer_class = ImageTaskSerializer
    queryset = ImageTask.objects.all()
    permission_classes = [IsAuthenticated]
