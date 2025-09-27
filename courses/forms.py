from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .models import Course


class CourseEnrollmentForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects.filter(is_active=True),
        label="Kurs",
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
    experience_level = forms.ChoiceField(
        choices=[
            ('beginner', 'Boshlang\'ich'),
            ('intermediate', 'O\'rta'),
            ('advanced', 'Yuqori')
        ],
        label="Tajriba darajasi",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    additional_info = forms.CharField(
        required=False,
        label="Qo'shimcha ma'lumot",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Qo\'shimcha ma\'lumot (ixtiyoriy)'
        })
    )

    def send_enrollment_email(self):
        course = self.cleaned_data['course']
        subject = f"Kursga yozilish: {course.name}"
        message = f"""
        Yangi kursga yozilish so'rovi:

        Kurs: {course.name}
        Ism: {self.cleaned_data['full_name']}
        Email: {self.cleaned_data['email']}
        Telefon: {self.cleaned_data['phone']}
        Tajriba darajasi: {self.get_experience_level_display()}

        Qo'shimcha ma'lumot:
        {self.cleaned_data.get('additional_info', 'Yo\'q')}
        """

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['courses@kursmarkazi.uz'],
                fail_silently=False,
            )
            return True
        except:
            return False

    def get_experience_level_display(self):
        levels = dict(self.fields['experience_level'].choices)
        return levels.get(self.cleaned_data['experience_level'])