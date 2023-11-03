from  django.urls import path
from .views import show_wishlist, edit_wishlist_ajax, get_wishlist_ajax, add_to_wishlist, delete_wishlist_ajax

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('add-wishlist/', add_to_wishlist, name='add_wishlist'),
    path('get-wishlist/', get_wishlist_ajax, name='get_wishlist'),
    path('delete-wishlist/<int:wishlist_id>', delete_wishlist_ajax, name='delete_wishlist'),
]