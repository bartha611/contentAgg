from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager

# Create your models here.


class Profile(AbstractBaseUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    objects = CustomUserManager()

    REQUIRED_FIELDS = [first_name, last_name]
    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.email
