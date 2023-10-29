from django.contrib import admin
from django.urls import path, include
from resensi.views import book_list, book_detail, add_review

app_name = 'resensi'

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('book/<int:book_id>/add_review/', add_review, name='add_review'),
    
]