from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User


class feedback(models.Model):
    user = models.CharField('name', max_length=100)
    value = models.CharField('value', max_length=1000)


class UserNotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField('title', max_length=1000)
    value = models.TextField()

    def __str__(self):
        return self.title


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# class UserData(models.Model):
#     user = models.CharField('userid', max_length=100)
#     notes = models.ForeignKey(
#         UserNotes, on_delete=models.CASCADE, default=None, null=True)
#     todo = models.ForeignKey(
#         Todo, on_delete=models.CASCADE, default=None, null=True)

#     def __str__(self):
#         return self.user

#     class Meta:
#         ordering = ['user']
