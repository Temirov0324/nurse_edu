from django.urls import path
from . import views

app_name = 'vacancies'

urlpatterns = [
    path('', views.vacancy_list, name='list'),
    path('<int:pk>/', views.vacancy_detail, name='detail'),
    path('application/', views.job_application, name='application'),
    path('application/<int:pk>/', views.job_application, name='application_with_vacancy'),
]