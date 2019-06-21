from django.db import models
from django.urls import reverse

# Create your models here.

class Wish(models.Model):
    description = models.TextField(max_length=300)
