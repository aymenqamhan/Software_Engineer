from django.db import models

class Teacher(models.Model):
    LEVELS = [
        ('DR', 'DR'),
        ('PROF', 'PROF'),
        ('MASTER', 'MASTER'),
        ('STU', 'STU'),
    ]
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    age = models.IntegerField()
    level = models.CharField(choices=LEVELS, max_length=10)
    subject = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    report = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name} ({self.level})"

