from django.db import models

# Create your models here.
class Students(models.Model):
    Levels=[('1','1'),('2','2'),('3','3'),('4','4')]
    f_name = models.CharField(max_length=10,default="student")
    l_name = models.CharField(max_length=10,default="student")
    age = models.IntegerField()
    lavel = models.CharField(choices=Levels,max_length=20)
    gpa=models.DecimalField(max_digits=4, decimal_places=2)
    status=models.BooleanField(null=False)
    reporet = models.TextField(max_length=300)
    def __str__(self):
        return f"{self.f_name} {self.l_name}"
    
    # Create your models here.
class Tetchers(models.Model):
    him_marks=[('DR','DR'),('PROF','PROF'),('MASTER','MASTER'),('STU','STU')]
    f_name = models.CharField(max_length=10,default="student")
    l_name = models.CharField(max_length=10,default="student")
    age = models.IntegerField()
    lavel = models.CharField(choices=him_marks,max_length=20)
    book_tetch=models.CharField(max_length=20,default="programmer")
    status=models.BooleanField(null=False)
    reporet = models.TextField(max_length=300)
    def __str__(self):
        return f"{self.f_name} {self.l_name} {self.lavel}"