from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.firstpage),
    path('posts/<int:post>/', views.postes),
    path('aboutproject/', views.aboutproject),
    path('redsquad/', views.redsquad),
]