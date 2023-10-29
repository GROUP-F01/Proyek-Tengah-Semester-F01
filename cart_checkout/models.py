from django.db import models

# Create your models here.
class Checkout(models.Model):
    nama_pembeli = models.CharField(null=True, blank=True, max_length=255)
    alamat = models.TextField(null=True, blank=True)