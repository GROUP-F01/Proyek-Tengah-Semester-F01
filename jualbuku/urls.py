from django.urls import path
from jualbuku.views import *

app_name = 'jualbuku'

urlpatterns = [
    path('', show_buku, name='jual_buku'),
    path('create-buku', create_buku, name='create_buku'),
    path('show-json', show_json),
    path('show-xml', show_xml),
    path('all_buku_flutter/', all_buku_flutter, name='all_buku_flutter'),
    path('show_buku_flutter/', show_buku_flutter, name='show_buku_flutter'),
    path('create_buku_flutter/', create_buku_flutter, name='create_buku_flutter'),
    path('update_buku_flutter/', update_buku_flutter, name='update_buku_flutter'),
    path('delete_buku_flutter/', delete_buku_flutter, name='delete_buku_flutter'),
]