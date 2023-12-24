from django.db import models

# Create your models here.
class Project(models.Model):
    titulo=models.CharField(max_length=200)
    descripcion=models.TextField()
    tecnologias=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)