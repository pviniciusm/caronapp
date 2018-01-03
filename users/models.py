from django.db import models
from django.utils import timezone


# Create your models here.
class Puser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'self.name+"-"+self.id'