from django.db import models
from main.models import Buku
from django.contrib.auth.models import User

class Review(models.Model):
    book = models.ForeignKey(Buku, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()

    def __str__(self):
        return f"{self.user}'s review for {self.book.title}"
