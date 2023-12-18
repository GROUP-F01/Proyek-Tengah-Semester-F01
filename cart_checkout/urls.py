from django.urls import path
from cart_checkout.views import *

app_name = 'cart_checkout'

urlpatterns = [
    path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('book_checkout', book_checkout, name="book_checkout"),
    path('inventory', inventory, name="inventory"),
    path('delete_book/<str:book_title>', delete_book, name='delete_book'), 
    path('delete_book_ajax/<str:book_title>/', delete_book_ajax, name='delete_book_ajax'),
    path('show_keranjang/', show_keranjang, name='show_keranjang'),
    path('list_keranjang/', list_keranjang, name='list_keranjang'),
    path('ambil_buku/', ambil_buku, name='ambil_buku'),
    path('tambah_keranjang/', tambah_keranjang, name='tambah_keranjang'),
    path('delete_buku/', delete_buku, name='delete_buku'),
    path('checkout_keranjang/', checkout_keranjang, name='checkout_keranjang'),
]