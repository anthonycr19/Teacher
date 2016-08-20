from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    student = models.ManyToManyField(Student, related_name='students')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
