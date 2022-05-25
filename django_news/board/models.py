from django.db import models

class Announs(models.Model):
    header = models.CharField(max_length=150)
    Author = models.CharField(max_length=150, blank=True)
    text = models.TextField()

    def __str__(self):
       return self.header
