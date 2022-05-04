from django.urls import path
from . import  views

app_name = 'watermelon'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail')
]
