from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser




# Create your models here.
class Puser(AbstractUser):
    birthday = models.DateField(null=True)

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        d_name = ""+str(self.username)+"-"+str(self.id)
        return d_name