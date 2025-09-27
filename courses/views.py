from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, CourseModule
from .forms import CourseEnrollmentForm


def course_list(request):
    courses = Course.objects.filter(is_active=True)
    context = {
        'courses': courses,
    }
    return render(request, 'courses/list.html', context)


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk, is_active=True)
    modules = CourseModule.objects.filter(course=course, is_active=True)
    context = {
        'course': course,
        'modules': modules,
    }
    return render(request, 'courses/detail.html', context)


def course_enrollment(request, pk=None):
    if request.method == 'POST':
        form = CourseEnrollmentForm(request.POST)
        if form.is_valid():
            if form.send_enrollment_email():
                messages.success(request, 'Kursga yozilish so\'rovi muvaffaqiyatli yuborildi!')
                return redirect('courses:list')
            else:
                messages.error(request, 'So\'rov yuborishda xatolik yuz berdi.')
    else:
        initial_data = {}
        if pk:
            course = get_object_or_404(Course, pk=pk, is_active=True)
            initial_data['course'] = course
        form = CourseEnrollmentForm(initial=initial_data)

    context = {
        'form': form,
    }
    return render(request, 'courses/enrollment.html', context)