from django.contrib import admin
from .models import Certificate, StudentCertificate

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'certificate_type', 'is_active', 'created_at')
    list_filter = ('certificate_type', 'is_active', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('is_active',)

@admin.register(StudentCertificate)
class StudentCertificateAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'certificate', 'issue_date', 'certificate_number', 'is_verified')
    list_filter = ('certificate', 'is_verified', 'issue_date')
    search_fields = ('student_name', 'student_email', 'certificate_number')
    list_editable = ('is_verified',)
    date_hierarchy = 'issue_date'