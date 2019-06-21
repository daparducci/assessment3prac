from django.db import models
from django.urls import reverse

# Create your models here.

class Skill(models.Model):
    description = models.TextField(max_length=300)
