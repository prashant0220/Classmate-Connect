from django.db import models
from datetime import date


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=100)  # Note: In practice, you should use a more secure way to store pass
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    default_dob = date(2000, 1, 1)
    dob = models.DateField(default=default_dob)

    def __str__(self):
        return self.name
