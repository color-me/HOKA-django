from django.contrib.auth.models import AbstractUser
from django.db import models


class USER(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)


class Driver(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    num = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    carNum = models.CharField(max_length=20, blank=True, null=True)


class Tousu(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    sex = models.CharField(max_length=20, blank=True, null=True)
    num = models.CharField(max_length=20, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    reason = models.CharField(max_length=20, blank=True, null=True)
