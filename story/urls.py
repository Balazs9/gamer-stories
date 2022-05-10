from . import views
from django.urls import path


urlpatterns = [
    path('', views.Stories.as_view(), name="home"),
    path('create/', views.StorieCreate.as_view(), name="storie_create"),
]
