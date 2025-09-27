from django.shortcuts import render, get_object_or_404
from .models import Specialist

def specialist_list(request):
    specialists = Specialist.objects.filter(is_active=True)
    context = {
        'specialists': specialists,
    }
    return render(request, 'specialists/list.html', context)

def specialist_detail(request, pk):
    specialist = get_object_or_404(Specialist, pk=pk, is_active=True)
    context = {
        'specialist': specialist,
    }
    return render(request, 'specialists/detail.html', context)