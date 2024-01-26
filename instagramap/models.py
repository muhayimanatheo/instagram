from django.db import models

# Create your models here.
class myProfile(models.Model):
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    button = models.CharField(max_length=100)
    bio = models.TextField(max_length=100)

    def __str__(self):
        return self.username

class Gallery(models.Model):
    image = models.ImageField(upload_to='images/')    