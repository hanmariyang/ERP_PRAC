from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class UserModel(AbstractUser):

    class Meta:
        db_table = "my_user"
    
    bio = models.TextField(max_length=500, blank=True)