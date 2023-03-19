from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email adress', unique=True)
    phone = models.CharField(max_length=12)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email