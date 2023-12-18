from django.db import models
from main.models import Buku
from django.contrib.auth.models import User

class Resensi(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    book = models.ForeignKey(Buku, on_delete=models.CASCADE)
    published_by = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now_add=True)
    resensi = models.TextField()