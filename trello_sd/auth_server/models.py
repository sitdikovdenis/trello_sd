from django.db import models


class SubDivision(models.Model):
    name = models.CharField(max_length=512)


class Employee(models.Model):
    surname = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    patronymic = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    subdivision = models.ForeignKey(SubDivision, on_delete=models.SET_NULL, related_name='subdivision')
    email = models.EmailField()
