from django.db import models
import math

class Circle(models.Model):
    radius = models.FloatField()

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle with radius {self.radius}"