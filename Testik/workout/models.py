from django.db import models

class Workout(models.Model):
    part = models.CharField(max_length=20)
    exercises = models.IntegerField()
    duration = models.IntegerField()
