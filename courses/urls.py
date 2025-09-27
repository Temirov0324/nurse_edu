from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='list'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('enrollment/', views.course_enrollment, name='enrollment'),
    path('enrollment/<int:pk>/', views.course_enrollment, name='enrollment_with_course'),
]