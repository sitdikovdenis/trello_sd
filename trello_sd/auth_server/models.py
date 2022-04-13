import random
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class SubDivision(models.Model):
    directum_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return f'{self.surname} {self.name}'


class MirricoManagementUser2(AbstractUser):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='employee', null=True)
    patronymic = models.CharField(max_length=256)
    confirmed = models.BooleanField(default=False)


class RegisterVerificationMailing(models.Model):
    email = models.EmailField()
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    sent = models.BooleanField(default=False)


class RegisterVerificationCode(models.Model):
    STATE_CHOICES = (
        ('A', 'Active'),
        ('C', 'Close'),
    )
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reg_ver_code_employee')
    code = models.CharField(max_length=6)
    create_at = models.DateTimeField(auto_now_add=True)
    sent_time = models.DateTimeField(null=True, blank=True)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='A')

    def __str__(self):
        return f'{self.employee.directum_id}; {self.code}'
