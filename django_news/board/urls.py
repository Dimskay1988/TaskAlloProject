from django.urls import path
from . import views

urlpatterns = [
    path('announce/', views.annouce),
]