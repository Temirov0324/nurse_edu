from django.urls import path
from . import views

app_name = 'specialists'

urlpatterns = [
    path('', views.specialist_list, name='list'),
    path('<int:pk>/', views.specialist_detail, name='detail'),
]