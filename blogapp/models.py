from django.db import models
from django.utils import timezone


class Post(models.Model):
    titulo = models.CharField(max_length=300)
    texto = models.TextField()

    def publicar(self):
        self.save()

    def __str__(self):
        return self.titulo
