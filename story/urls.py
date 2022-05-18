from . import views
from django.urls import path

urlpatterns = [
    path('userstory/', views.UserStory.as_view(), name='user_stories'),
    path('create/', views.StorieCreate.as_view(), name='storie_create'),
    path('<pk>/', views.PostStorieDetail.as_view(), name='poststorie_detail'),
    path('<pk>/update', views.StorieUpdate.as_view(), name='storie_update'),
    path('<pk>/delete/', views.StorieDelete.as_view(), name='storie_delete'),
]
