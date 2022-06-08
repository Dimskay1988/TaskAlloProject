from django.urls import path
from . import views

urlpatterns = [
    path('announce/', views.annouce),
    path('announce/<int:post>/', views.newfilter),
    path('announce/create/', views.createannounce),
    path('announce/delete/<int:post>', views.deleteannounce),
]