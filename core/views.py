from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import AboutInfo
from .forms import ContactForm
from news.models import News
from departments.models import Department
from courses.models import Course


def index(request):
    about_info = AboutInfo.objects.filter(is_active=True).first()
    latest_news = News.objects.filter(is_published=True)[:3]
    departments = Department.objects.filter(is_active=True)[:6]
    courses = Course.objects.filter(is_active=True)[:4]

    context = {
        'about_info': about_info,
        'latest_news': latest_news,
        'departments': departments,
        'courses': courses,
    }
    return render(request, 'core/index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            if form.send_email():
                messages.success(request, 'Xabaringiz muvaffaqiyatli yuborildi!')
                return redirect('core:contact')
            else:
                messages.error(request, 'Xabar yuborishda xatolik yuz berdi.')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'core/contact.html', context)