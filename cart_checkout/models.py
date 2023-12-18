from django.db import models
from main.models import Buku
from django.contrib.auth.models import User

# Create your models here.
class Checkout(models.Model):
    nama_pembeli = models.CharField(null=True, blank=True, max_length=255)
    alamat = models.TextField(null=True, blank=True)

class BeliBuku(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    jumlah = models.IntegerField(default=0)
    total_harga = models.IntegerField(default=0)

class Keranjang(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    harga = models.IntegerField(default=0)
    list_buku = models.ManyToManyField(BeliBuku)