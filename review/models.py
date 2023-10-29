from django.db import models
from main.models import User,Buku
from rest_framework import serializers

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    RATING_CHOICES = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),)
    rating = models.IntegerField(choices=RATING_CHOICES)
    review = models.TextField()

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    buku = BukuSerializer()

    class Meta:
        model = Review
        fields = '__all__'