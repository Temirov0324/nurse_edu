from django.contrib import admin
from .models import Specialist

@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'experience_years', 'is_active', 'created_at')
    list_filter = ('specialization', 'is_active', 'experience_years')
    search_fields = ('full_name', 'specialization', 'bio')
    list_editable = ('is_active',)