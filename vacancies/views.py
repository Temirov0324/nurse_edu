from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Vacancy
from .forms import JobApplicationForm


def vacancy_list(request):
    vacancies = Vacancy.objects.filter(is_active=True)
    context = {
        'vacancies': vacancies,
    }
    return render(request, 'vacancies/list.html', context)


def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk, is_active=True)
    context = {
        'vacancy': vacancy,
    }
    return render(request, 'vacancies/detail.html', context)


def job_application(request, pk=None):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            if form.send_application_email():
                messages.success(request, 'Arizangiz muvaffaqiyatli yuborildi!')
                return redirect('vacancies:list')
            else:
                messages.error(request, 'Ariza yuborishda xatolik yuz berdi.')
    else:
        initial_data = {}
        if pk:
            vacancy = get_object_or_404(Vacancy, pk=pk, is_active=True)
            initial_data['vacancy'] = vacancy
        form = JobApplicationForm(initial=initial_data)

    context = {
        'form': form,
    }
    return render(request, 'vacancies/application.html', context)