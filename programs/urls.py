from django.urls import path
from . import views

app_name = 'programs'

urlpatterns = [
    path('', views.direction_list, name='direction_list'),
    path('directions/<int:pk>/', views.direction_detail, name='direction_detail'),
    path('specializations/<int:pk>/', views.specialization_detail, name='specialization_detail'),
    path('study-plans/<int:pk>/', views.study_plan_detail, name='study_plan_detail'),
]