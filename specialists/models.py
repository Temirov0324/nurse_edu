from django.db import models

class Specialist(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="F.I.Sh.")
    specialization = models.CharField(max_length=200, verbose_name="Mutaxassislik")
    experience_years = models.PositiveIntegerField(verbose_name="Tajriba yillari")
    photo = models.ImageField(upload_to='specialists/', blank=True, null=True, verbose_name="Surat")
    bio = models.TextField(verbose_name="Qisqacha ma'lumot")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mutaxassis"
        verbose_name_plural = "Mutaxassislar"
        ordering = ['full_name']

    def __str__(self):
        return self.full_name