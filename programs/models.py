from django.db import models


class Direction(models.Model):
    name = models.CharField(max_length=200, verbose_name="Yo'nalish nomi")
    description = models.TextField(verbose_name="Ta'rif")
    image = models.ImageField(
        upload_to='directions/',
        blank=True,
        null=True,
        verbose_name="Rasm"
    )
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Yo'nalish"
        verbose_name_plural = "Yo'nalishlar"
        ordering = ['name']

    def __str__(self):
        return self.name


class Specialization(models.Model):
    direction = models.ForeignKey(
        Direction,
        on_delete=models.CASCADE,
        related_name='specializations',
        verbose_name="Yo'nalish"
    )
    name = models.CharField(max_length=200, verbose_name="Mutaxassislik nomi")
    description = models.TextField(verbose_name="Ta'rif")
    duration = models.CharField(max_length=100, verbose_name="Davomiyligi")
    requirements = models.TextField(verbose_name="Kirish talablari")
    career_prospects = models.TextField(verbose_name="Karyera imkoniyatlari")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mutaxassislik"
        verbose_name_plural = "Mutaxassisliklar"
        ordering = ['name']

    def __str__(self):
        return f"{self.direction.name} - {self.name}"


class StudyPlan(models.Model):
    PLAN_TYPES = [
        ('annual', 'Yillik reja'),
        ('semester', 'Semestr rejasi'),
        ('monthly', 'Oylik reja'),
        ('weekly', 'Haftalik reja'),
    ]

    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
        related_name='study_plans',
        verbose_name="Mutaxassislik"
    )
    title = models.CharField(max_length=200, verbose_name="Reja nomi")
    plan_type = models.CharField(
        max_length=20,
        choices=PLAN_TYPES,
        default='semester',
        verbose_name="Reja turi"
    )
    academic_year = models.CharField(
        max_length=20,
        verbose_name="O'quv yili",
        help_text="Masalan: 2024-2025"
    )
    semester = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name="Semestr raqami"
    )
    description = models.TextField(verbose_name="Ta'rif")
    file = models.FileField(
        upload_to='study_plans/',
        blank=True,
        null=True,
        verbose_name="Reja fayli (PDF)"
    )
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "O'quv rejasi"
        verbose_name_plural = "O'quv rejalari"
        ordering = ['-academic_year', 'semester']

    def __str__(self):
        return f"{self.specialization.name} - {self.title}"


class Subject(models.Model):
    study_plan = models.ForeignKey(
        StudyPlan,
        on_delete=models.CASCADE,
        related_name='subjects',
        verbose_name="O'quv rejasi"
    )
    name = models.CharField(max_length=200, verbose_name="Fan nomi")
    code = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Fan kodi"
    )
    credits = models.PositiveIntegerField(verbose_name="Kredit soatlari")
    lecture_hours = models.PositiveIntegerField(
        default=0,
        verbose_name="Ma'ruza soatlari"
    )
    practical_hours = models.PositiveIntegerField(
        default=0,
        verbose_name="Amaliy mashg'ulot soatlari"
    )
    laboratory_hours = models.PositiveIntegerField(
        default=0,
        verbose_name="Laboratoriya soatlari"
    )
    independent_hours = models.PositiveIntegerField(
        default=0,
        verbose_name="Mustaqil ish soatlari"
    )
    prerequisites = models.TextField(
        blank=True,
        null=True,
        verbose_name="Oldindan o'rganilishi kerak fanlar"
    )
    description = models.TextField(verbose_name="Fan haqida ma'lumot")
    order = models.PositiveIntegerField(default=1, verbose_name="Tartib raqami")

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.credits} kredit)"

    @property
    def total_hours(self):
        return (self.lecture_hours + self.practical_hours +
                self.laboratory_hours + self.independent_hours)