from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .models import Vacancy


class JobApplicationForm(forms.Form):
    vacancy = forms.ModelChoiceField(
        queryset=Vacancy.objects.filter(is_active=True),
        label="Vakansiya",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    full_name = forms.CharField(
        max_length=100,
        label="To'liq ism",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ismingizni kiriting'
        })
    )
    email = forms.EmailField(
        label="Email manzil",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'email@example.com'
        })
    )
    phone = forms.CharField(
        max_length=20,
        label="Telefon raqam",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+998 90 123 45 67'
        })
    )
    education = forms.CharField(
        max_length=200,
        label="Ta'lim",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Oliy ta\'lim, mutaxassislik'
        })
    )
    experience = forms.CharField(
        label="Ish tajribasi",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Ish tajribangiz haqida yozing...'
        })
    )
    cv_file = forms.FileField(
        required=False,
        label="CV fayli",
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.pdf,.doc,.docx'
        })
    )
    cover_letter = forms.CharField(
        required=False,
        label="Motivatsion xat",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Nega aynan siz uchun ish bermoqchisiz?'
        })
    )

    def send_application_email(self):
        vacancy = self.cleaned_data['vacancy']
        subject = f"Ish uchun ariza: {vacancy.position}"
        message = f"""
        Yangi ish uchun ariza:

        Vakansiya: {vacancy.position}
        Ism: {self.cleaned_data['full_name']}
        Email: {self.cleaned_data['email']}
        Telefon: {self.cleaned_data['phone']}
        Ta'lim: {self.cleaned_data['education']}

        Ish tajribasi:
        {self.cleaned_data['experience']}

        Motivatsion xat:
        {self.cleaned_data.get('cover_letter', 'Yo\'q')}
        """

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [vacancy.contact_email],
                fail_silently=False,
            )
            return True
        except:
            return False