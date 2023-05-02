from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class NewUser(AbstractUser):
    avatar = models.FileField(("Avatar"), upload_to="Avatar", max_length=100)