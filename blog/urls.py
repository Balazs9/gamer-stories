from . import views
from django.urls import path


urlpatterns = [
    path('', views.StorieList.as_view(), name='home')
]