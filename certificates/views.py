from django.shortcuts import render, get_object_or_404
from .models import Certificate, StudentCertificate


def certificate_list(request):
    certificates = Certificate.objects.filter(is_active=True)
    context = {
        'certificates': certificates,
    }
    return render(request, 'certificates/list.html', context)


def certificate_detail(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk, is_active=True)
    context = {
        'certificate': certificate,
    }
    return render(request, 'certificates/detail.html', context)


def certificate_verify(request):
    certificate = None
    error_message = None

    if request.method == 'GET' and 'number' in request.GET:
        certificate_number = request.GET.get('number')
        try:
            certificate = StudentCertificate.objects.get(
                certificate_number=certificate_number,
                is_verified=True
            )
        except StudentCertificate.DoesNotExist:
            error_message = "Sertifikat topilmadi yoki tasdiqlanmagan."

    context = {
        'certificate': certificate,
        'error_message': error_message,
    }
    return render(request, 'certificates/verify.html', context)