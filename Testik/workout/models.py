from django.db import models

class Workout(models.Model):
    part = models.CharField(max_length=20)
    exercises = models.IntegerField()
    duration = models.IntegerField()
    place = models.CharField(max_length=20, default="home")

    def __str__(self):
        return f"{self.id}: {self.part} for {self.duration}"
    

class Pohar(models.Model):
    identity = models.IntegerField(default="0")
    location = models.CharField(max_length=20, default="lost") 
    name = models.CharField(max_length=20, default="unidentified")
    origin = models.CharField(max_length=64, default="unknown")
    qrcode = models.CharField(max_length=20,)

    def __str__(self):
        return f"{self.name} na {self.location} od {self.origin}" 