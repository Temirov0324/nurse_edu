from django.shortcuts import render, get_object_or_404
from .models import Department

def department_list(request):
    departments = Department.objects.filter(is_active=True)
    context = {
        'departments': departments,
    }
    return render(request, 'departments/list.html', context)

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk, is_active=True)
    context = {
        'department': department,
    }
    return render(request, 'departments/detail.html', context)