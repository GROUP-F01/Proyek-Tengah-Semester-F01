from django.db import models
from main.models import Buku

class Review(models.Model):
    book = models.ForeignKey(Buku, on_delete=models.CASCADE, related_name='reviews')
    user = models.CharField(max_length=100)
    review_text = models.TextField()

    def __str__(self):
        return f"{self.user}'s review for {self.book.title}"
