from django.urls import path
from resensi.views import *

app_name = 'resensi'

urlpatterns = [
    path('get_resensi/', get_resensi, name='get_resensi'),
    path('get_book/', get_book, name='get_book'),
    path('resensi_buku/', resensi_buku, name='resensi_buku'),
    path('create_resensi/', create_resensi, name='create_resensi'),
    path('delete_resensi/', delete_resensi, name='delete_resensi'),
    path('edit_resensi/', edit_resensi, name='edit_resensi'),
]