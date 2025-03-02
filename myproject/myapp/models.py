from django.db import models
import math

class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200)