from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_comment/<str:pk>/', views.update_comment, name='update'),
    path('delete_comment/<str:pk>/', views.delete_comment, name='delete'),
]

