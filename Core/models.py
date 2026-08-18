from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    IS_ADMIN = 1
    IS_TEACHER = 2
    IS_STUDENT = 3
    
    ROLE_CHOICES = (
        (IS_ADMIN, 'Admin'),
        (IS_TEACHER, 'Teacher'),
        (IS_STUDENT, 'Student'),
    )
    user_type = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=3)


# Create your models here.
class Classroom(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.section})"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True)
    admission_number = models.CharField(max_length=50, unique=True)
    parent_phone = models.CharField(max_length=15)

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    exam_date = models.DateField()
