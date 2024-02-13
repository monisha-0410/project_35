from django.db import models

# Create your models here.
class School(models.Model):
    School_name=models.CharField(max_length=100)
    Scl_principal=models.CharField(max_length=100)