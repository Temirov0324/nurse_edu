from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name="Kurs nomi")
    description = models.TextField(verbose_name="Qisqacha ma'lumot")
    duration = models.CharField(max_length=100, verbose_name="Davomiyligi")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    image = models.ImageField(upload_to='courses/', blank=True, null=True, verbose_name="Rasm")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
        ordering = ['name']

    def __str__(self):
        return self.name

class CourseModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules', verbose_name="Kurs")
    title = models.CharField(max_length=200, verbose_name="Modul nomi")
    description = models.TextField(verbose_name="Ta'rif")
    order = models.PositiveIntegerField(default=1, verbose_name="Tartib raqami")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Kurs moduli"
        verbose_name_plural = "Kurs modullari"
        ordering = ['order']

    def __str__(self):
        return f"{self.course.name} - {self.title}"