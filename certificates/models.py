from django.db import models


class Certificate(models.Model):
    CERTIFICATE_TYPES = [
        ('completion', 'Kursni tugatish sertifikati'),
        ('achievement', 'Yutuq sertifikati'),
        ('participation', 'Ishtirok sertifikati'),
        ('professional', 'Professional sertifikat'),
    ]

    title = models.CharField(max_length=200, verbose_name="Sertifikat nomi")
    description = models.TextField(verbose_name="Ta'rif")
    certificate_type = models.CharField(
        max_length=20,
        choices=CERTIFICATE_TYPES,
        default='completion',
        verbose_name="Sertifikat turi"
    )
    requirements = models.TextField(verbose_name="Olish shartlari")
    validity_period = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Amal qilish muddati"
    )
    image = models.ImageField(
        upload_to='certificates/',
        blank=True,
        null=True,
        verbose_name="Sertifikat namunasi"
    )
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Sertifikat"
        verbose_name_plural = "Sertifikatlar"
        ordering = ['title']

    def __str__(self):
        return self.title


class StudentCertificate(models.Model):
    certificate = models.ForeignKey(
        Certificate,
        on_delete=models.CASCADE,
        verbose_name="Sertifikat"
    )
    student_name = models.CharField(max_length=200, verbose_name="Talaba ismi")
    student_email = models.EmailField(verbose_name="Email")
    issue_date = models.DateField(verbose_name="Berilgan sana")
    certificate_number = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Sertifikat raqami"
    )
    is_verified = models.BooleanField(default=False, verbose_name="Tasdiqlangan")

    class Meta:
        verbose_name = "Talaba sertifikati"
        verbose_name_plural = "Talaba sertifikatlari"
        ordering = ['-issue_date']

    def __str__(self):
        return f"{self.student_name} - {self.certificate.title}"