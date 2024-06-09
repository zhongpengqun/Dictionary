from django.db import models

# Create your models here.
class Word(models.Model):
    english = models.CharField(max_length=999)
    chinese = models.CharField(max_length=999)
