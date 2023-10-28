from django.urls import path
from jualbuku.views import show_buku
from jualbuku.views import create_buku

app_name = 'jualbuku'

urlpatterns = [
    path('', show_buku, name='jual_buku'),
    path('create-buku', create_buku, name='create_buku'),

]