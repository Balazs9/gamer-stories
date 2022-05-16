from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.StorieCreate.as_view(), name='storie_create'),
]
