from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Hellopage/', views.hellopage, name='hellopage'),
    path('YouarenotPrepared/', views.youarenotPrepared, name='youarenotPrepared'),
]
