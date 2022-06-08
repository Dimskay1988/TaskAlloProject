from django.db import models
from django.contrib import admin

class Announs(models.Model):
    header = models.CharField(max_length=150)
    Author = models.ForeignKey("Authorblog", on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
       return self.header

class ImagePost(Announs):
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    image_content = models.ImageField(upload_to='images', null=True, blank=True)

class Authorblog(models.Model):
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

admin.site.register(ImagePost)
admin.site.register (Authorblog)