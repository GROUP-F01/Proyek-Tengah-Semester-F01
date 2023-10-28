from django.db import models
from main.models import Buku
from django.contrib.auth.models import User

class BukuUser(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
