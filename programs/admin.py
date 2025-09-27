from django.contrib import admin
from .models import Direction, Specialization, StudyPlan, Subject

class SpecializationInline(admin.TabularInline):
    model = Specialization
    extra = 1

@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('is_active',)
    inlines = [SpecializationInline]

class StudyPlanInline(admin.TabularInline):
    model = StudyPlan
    extra = 1

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'direction', 'duration', 'is_active', 'created_at')
    list_filter = ('direction', 'is_active', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('is_active',)
    inlines = [StudyPlanInline]

class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 1
    fields = ('name', 'code', 'credits', 'lecture_hours', 'practical_hours', 'order')

@admin.register(StudyPlan)
class StudyPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'specialization', 'plan_type', 'academic_year', 'semester', 'is_active')
    list_filter = ('plan_type', 'academic_year', 'is_active', 'created_at')
    search_fields = ('title', 'specialization__name')
    list_editable = ('is_active',)
    inlines = [SubjectInline]

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'study_plan', 'credits', 'total_hours', 'order')
    list_filter = ('study_plan__specialization', 'credits')
    search_fields = ('name', 'code', 'description')
    list_editable = ('order',)