from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

app_name = 'main'

class Buku(models.Model):
    isbn = models.CharField(null=True, blank=True, max_length=255)
    title = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    author = models.CharField(null=True, blank=True, max_length=255)
    publisher = models.CharField(null=True, blank=True, max_length=255)
    publication_date = models.CharField(null=True, blank=True, max_length=255)
    page_count = models.IntegerField(null=True, blank=True)
    category = models.CharField(null=True, blank=True, max_length=255)
    image_url = models.URLField(null=True, blank=True)
    lang = models.CharField(null=True, blank=True, max_length=255)
    price = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.title