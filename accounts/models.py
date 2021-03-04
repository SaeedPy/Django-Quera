from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    
    address = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    date_joined = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True, verbose_name='email address')
    first_name = models.CharField(max_length=25, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='active')
    is_staff = models.BooleanField(default=False, verbose_name='staff status')
    is_superuser = models.BooleanField(default=False, verbose_name='superuser status')
    last_login = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=25, unique=True)