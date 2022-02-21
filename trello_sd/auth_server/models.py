from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid, random

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


class MirricoManagementUser2(AbstractUser):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='employee', null=True)
    patronymic = models.CharField(max_length=256)


class RegisterVerificationMailing(models.Model):
    email = models.EmailField()
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    sent = models.BooleanField(default=False)


class RegisterVerificationCode(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reg_ver_code_employee')
    code = models.CharField(max_length=6, default=random.randint(0, 999999))
    create_at = models.DateTimeField(auto_now_add=True)
    sent_time = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.employee.directum_id}; {self.code}'
