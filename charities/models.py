from django.db import models
from django.db.models import Q

from accounts.models import User


class Benefactor(models.Model):
    EXPERIENCE_CHOICES = (
        (0, 'Beginner'),
        (1, 'Intermediate'),
        (2, 'Expert')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(choices=EXPERIENCE_CHOICES, default=0)
    free_time_per_week = models.PositiveIntegerField(default=0)

class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        return self.filter(charity__user=user).exclude(charity__user=None)

    def related_tasks_to_benefactor(self, user):
        return self.filter(assigned_benefactor__user=user).exclude(assigned_benefactor__user=None)

    def all_related_tasks_to_user(self, user):
        return self.filter(Q(state='P') | Q(charity__user=user) | Q(assigned_benefactor__user=user))


class Task(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    STATE_CHOICES = (
        ('P', 'Pending'),
        ('W', 'Waitting'),
        ('A', 'Assigend'),
        ('D', 'Done')
    )
    assigned_benefactor = models.ForeignKey(Benefactor, null=True, on_delete=models.SET_NULL)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(blank=True, null=True)
    age_limit_to = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    descriptions = models.TextField(blank=True, null=True)
    gender_limit = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True, null=True)
    state = models.CharField(choices=STATE_CHOICES, max_length=1, default='P')
    title = models.CharField(max_length=100)
    
    objects = TaskManager()