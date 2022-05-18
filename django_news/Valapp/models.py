from django.db import models

class Article(models.Model):
    header = models.CharField(max_length=150)
    Author = models.CharField(max_length=150)
    text = models.TextField(blank=False, null=False, default='This is text')
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)
