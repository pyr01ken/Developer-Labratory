from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField()
    volume = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    expiration_time = models.CharField()
