from django.db import models
from django.contrib.auth import get_user_model
from plans.models import Plan
from teams.models import Team

User = get_user_model()


class FileManager(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'developer_laboratory_file_manager'

    def __str__(self):
        return f'{self.name} - {self.user.first_name}'
