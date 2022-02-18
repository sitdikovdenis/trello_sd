from django.db import models
from django.contrib.auth.models import AbstractUser


class SubDivision(models.Model):
    directum_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=512)


class Employee(models.Model):
    STATE_CHOICES = (
        ('Д', 'Действующая'),
        ('З', 'Закрытая'),
    )

    directum_id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    patronymic = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    subdivision = models.ForeignKey(SubDivision, on_delete=models.SET_NULL, related_name='subdivision', null=True)
    email = models.EmailField()
    state = models.CharField(max_length=20, choices=STATE_CHOICES)


class AppUser(AbstractUser):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='employee')
