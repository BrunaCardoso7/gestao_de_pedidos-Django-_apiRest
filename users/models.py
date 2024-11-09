from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=12, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=150, null=False, blank=False, unique=True)
    password = models.CharField(max_length=32, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(null=False, blank=False)
