from django.db import models

# Create your models here.

class Tasks(models.Model):
    titulo = models.CharField(max_length=128)
    done = models.BooleanField(default=True)
    data = models.DateTimeField(auto_now_add=True)
    doTo = models.TextField(null=True, blank=True)
    projeto = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo
