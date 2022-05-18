from . import views
from django.urls import path


urlpatterns = [
    path('', views.StorieList.as_view(), name='home'),
    path('<int:pk>/detail', views.StorieDetail.as_view(), name='storie_detail'),
    path('like/<int:pk>', views.StorieLike.as_view(), name='storie_like'),
    path('<int:pk>/update', views.StorieUpdate.as_view(), name='storie_update'),
    path('<int:pk>/delete/', views.StorieDelete.as_view(), name='storie_delete'),
]
