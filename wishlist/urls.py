from django.urls import path
from .views import (add_to_wishlist, add_wishlist_ajax, delete_wishlist_ajax,
                    edit_wishlist_ajax, get_wishlist_ajax, show_wishlist)

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('add-wishlist/', add_to_wishlist, name='add_wishlist'),
    path('get-wishlist/', get_wishlist_ajax, name='get_wishlist'),
    path('delete-wishlist/<int:wishlist_id>', delete_wishlist_ajax, name='delete_wishlist'),
    path('add-wishlist-ajax/', add_wishlist_ajax, name='add_wishlist_ajax')
]