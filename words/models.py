from django.db import models


# Create your models here.
class Word(models.Model):
    name = models.CharField(max_length=128, unique=True)
    meaning = models.TextField()

    def __str__(self):
        return self.name
