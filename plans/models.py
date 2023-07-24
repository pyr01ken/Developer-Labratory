from django.db import models
from django.contrib.auth import get_user_model
from teams.models import Team  # todo: fix import bug.

User = get_user_model()


class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    body = models.TextField()
    volume = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    expiration_days = models.CharField(max_length=100)

    class Meta:
        db_table = "developer_laboratory_plans"

    def __str__(self):
        return self.name


class FileManager(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'developer_laboratory_file_manager'
