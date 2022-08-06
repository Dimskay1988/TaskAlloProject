from rest_framework import viewsets, response
from .serializers import ConnectSerializer
from .models import Comment

class CommentViewSet(viewsets.ModelViewSet):
    """Список всех коментов"""
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class ImageCommentViewSet(viewsets.ModelViewSet):
    """Список всех изображений для комментов"""
    serializer_class = ImageCommentSerializer
    queryset = ImageComment.objects.all()
