from . import views
from django.urls import path


urlpatterns = [
    path('', views.StorieList.as_view(), name='home'),
    path('<slug:slug>/', views.StorieDetail.as_view(), name='storie_detail'),
    path('like/<slug:slug>', views.StorieLike.as_view(), name='storie_like'),
    path('create/<slug:slug>', views.StorieCreate.as_view(), name='storie_create'),
]