from django.db import models

class Vacancy(models.Model):
    position = models.CharField(max_length=200, verbose_name="Lavozim nomi")
    requirements = models.TextField(verbose_name="Talablar")
    salary = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ish haqi")
    contact_email = models.EmailField(verbose_name="Murojaat email manzili")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Vakansiya"
        verbose_name_plural = "Vakansiyalar"
        ordering = ['-created_at']

    def __str__(self):
        return self.position