from django.db import models
from numpy import set_printoptions

# Create your models here.

class Post(models.Model) :
    judul = models.CharField(max_length=255)
    sinopsis = models.TextField()

    def __str__(self) :
        return self.judul