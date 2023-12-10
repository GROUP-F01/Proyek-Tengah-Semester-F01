from django.urls import path
from jualbuku.views import *

app_name = 'jualbuku'

urlpatterns = [
    path('', show_buku, name='jual_buku'),
    path('create-buku', create_buku, name='create_buku'),
    path('show-json', show_json),
    path('show-xml', show_xml)

]