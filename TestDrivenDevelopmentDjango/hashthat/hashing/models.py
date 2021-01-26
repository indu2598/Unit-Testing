from django.db import models

# Create your models here.
class HashModel(models.Model):
    text = models.TextField()
    hash = models.CharField(max_length=64)