from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactForm(forms.Form):
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
    subject = forms.CharField(
        max_length=200,
        label="Mavzu",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Xabar mavzusi'
        })
    )
    message = forms.CharField(
        label="Xabar",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Xabaringizni yozing...'
        })
    )

    def send_email(self):
        subject = f"Saytdan xabar: {self.cleaned_data['subject']}"
        message = f"""
        Ism: {self.cleaned_data['full_name']}
        Email: {self.cleaned_data['email']}
        Telefon: {self.cleaned_data['phone']}

        Xabar:
        {self.cleaned_data['message']}
        """

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['admin@kursmarkazi.uz'],  # Admin email
                fail_silently=False,
            )
            return True
        except:
            return False