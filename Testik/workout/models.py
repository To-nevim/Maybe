from django.db import models

class Workout(models.Model):
    part = models.CharField(max_length=20)
    exercises = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.part} for {self.duration}"