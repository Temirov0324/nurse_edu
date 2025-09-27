from django.db import models

class AboutInfo(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Ta'rif")
    image = models.ImageField(upload_to='about/', blank=True, null=True, verbose_name="Rasm")
    video_url = models.URLField(blank=True, null=True, verbose_name="Video URL")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Biz haqimizda"
        verbose_name_plural = "Biz haqimizda ma'lumotlar"

    def __str__(self):
        return self.title