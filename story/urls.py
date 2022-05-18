from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.StorieCreate.as_view(), name='storie_create'),
    path('<pk>/', views.PostStorieDetail.as_view(), name='poststorie_detail'),
    path('<int:pk>/userupdate', views.UserStorieUpdate.as_view(), name='user_storie_update'),
    path('<int:pk>/userdelete/', views.UserStorieDelete.as_view(), name='user_storie_delete'),
]
