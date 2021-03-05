from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
        )

    address = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, verbose_name='email address')
    first_name = models.CharField(max_length=150, null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True, choices=GENDER_CHOICES)
    last_login = models.DateTimeField(null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
