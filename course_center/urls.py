
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('departments/', include('departments.urls')),
    path('news/', include('news.urls')),
    path('specialists/', include('specialists.urls')),
    path('vacancies/', include('vacancies.urls')),
    path('courses/', include('courses.urls')),
    path('certificates/', include('certificates.urls')),
    path('programs/', include('programs.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)