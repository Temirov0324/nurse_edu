from django.urls import path
from . import views

app_name = 'certificates'

urlpatterns = [
    path('', views.certificate_list, name='list'),
    path('<int:pk>/', views.certificate_detail, name='detail'),
    path('verify/', views.certificate_verify, name='verify'),
]