from django.shortcuts import render, get_object_or_404
from .models import Direction, Specialization, StudyPlan, Subject


def direction_list(request):
    directions = Direction.objects.filter(is_active=True)
    context = {
        'directions': directions,
    }
    return render(request, 'programs/direction_list.html', context)


def direction_detail(request, pk):
    direction = get_object_or_404(Direction, pk=pk, is_active=True)
    specializations = Specialization.objects.filter(
        direction=direction,
        is_active=True
    )
    context = {
        'direction': direction,
        'specializations': specializations,
    }
    return render(request, 'programs/direction_detail.html', context)


def specialization_detail(request, pk):
    specialization = get_object_or_404(Specialization, pk=pk, is_active=True)
    study_plans = StudyPlan.objects.filter(
        specialization=specialization,
        is_active=True
    )
    context = {
        'specialization': specialization,
        'study_plans': study_plans,
    }
    return render(request, 'programs/specialization_detail.html', context)


def study_plan_detail(request, pk):
    study_plan = get_object_or_404(StudyPlan, pk=pk, is_active=True)
    subjects = Subject.objects.filter(study_plan=study_plan)

    # Soatlarni hisoblash
    total_credits = sum(subject.credits for subject in subjects)
    total_hours = sum(subject.total_hours for subject in subjects)

    context = {
        'study_plan': study_plan,
        'subjects': subjects,
        'total_credits': total_credits,
        'total_hours': total_hours,
    }
    return render(request, 'programs/study_plan_detail.html', context)