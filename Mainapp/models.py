from django.db import models

# Create your models here.


class feedback(models.Model):
    user = models.CharField('name', max_length=100)
    value = models.CharField('value', max_length=1000)
