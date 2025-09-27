from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nomi")
    description = models.TextField(verbose_name="Ta'rif")
    image = models.ImageField(upload_to='departments/', blank=True, null=True, verbose_name="Rasm")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"
        ordering = ['name']

    def __str__(self):
        return self.name