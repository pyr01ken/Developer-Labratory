from django.db import models
from file_manager.models import FileManager
from teams.models import Team


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    body = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    file = models.ManyToManyField(FileManager)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated_at',)
        db_table = 'developer_laboratory_projects'

    def __str__(self):
        return f'{self.name} | {self.team}'

