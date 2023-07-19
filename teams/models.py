from django.db import models
from django.contrib.auth import get_user_model
from plans.models import Plan

User = get_user_model()


class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, through='TeamMembership')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TeamMembership(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_leader = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.team.name}"


class Task(models.Model):
    LOW = 1
    NORMAL = 2
    HIGH = 3

    PRIORITY_CHOICE = (
        (LOW, 'Low'),
        (NORMAL, 'Normal'),
        (HIGH, 'High'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField()
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

