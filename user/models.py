from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    ...


class Token(models.Model):
    key = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name='token')



