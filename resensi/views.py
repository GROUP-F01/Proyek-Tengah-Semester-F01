from django.shortcuts import render, get_object_or_404
from main.models import Buku
from resensi.models import Review
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Buku, Review


# Create your views here.

def book_list(request):
    books = Buku.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Buku, pk=book_id)
    reviews = book.reviews.all() 
    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews})

def add_review(request, book_id):
    book = get_object_or_404(Buku, pk=book_id)
    user = request.user
    review_text = request.POST['review_text']
    Review.objects.create(book=book, user=user, review_text=review_text)
    return HttpResponseRedirect(reverse('book_detail', args=(book.id,)))
