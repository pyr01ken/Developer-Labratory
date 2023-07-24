from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager


class User(AbstractBaseUser):
    TEAM_LEADER = 1
    TEAm_MEMBER = 2

    ROLE_CHOICE = (
        (TEAM_LEADER, "Team leader"),
        (TEAm_MEMBER, "Team member")
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    email_active_code = models.UUIDField(null=True, blank=True, unique=True)
    avatar = models.ImageField(upload_to='profiles/', null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    class Meta:
        db_table = 'developer_laboratory_accounts'
        ordering = ['-id']

    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'

    def get_role(self):
        user_role = None
        if self.role == 1:
            user_role = 'Team leader'
        elif self.role == 2:
            user_role = 'Team member'
        return user_role

    def __str__(self):
        return f'{self.get_fullname()} - {self.email}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
