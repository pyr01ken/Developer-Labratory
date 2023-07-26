from django.db import models
from django.contrib.auth import get_user_model
# todo: fix import bug
# from teams.models import Team

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