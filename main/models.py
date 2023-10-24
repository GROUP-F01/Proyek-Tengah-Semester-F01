from django.db import models

# Create your models here.
class Buku(models.Model):
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    year_published = models.IntegerField()