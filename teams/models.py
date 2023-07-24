from django.db import models
from django.contrib.auth import get_user_model
from plans.models import Plan

User = get_user_model()


class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leader_teams")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    members = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "developer_laboratory_teams"

    def __str__(self):
        return self.name


class Task(models.Model):
    LOW = 1
    NORMAL = 2
    HIGH = 3

    PRIORITY_CHOICE = (
        (LOW, 'Low'),
        (NORMAL, 'Normal'),
        (HIGH, 'High'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    body = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_tasks")
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "developer_laboratory_tasks"

    def __str__(self):
        return self.name
