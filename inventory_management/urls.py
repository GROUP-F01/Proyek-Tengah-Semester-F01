from django.urls import path
from inventory_management.views import admin_page, add_buku, register, login_user, logout_user, add_buku_ajax
from inventory_management.views import show_xml, show_json, show_xml_by_id, show_json_by_id, get_product_json

app_name = 'inventory_management'

urlpatterns = [
    path('literaloka-admin/', admin_page, name='literaloka_admin'),
    path('create-product', add_buku, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('add-buku-ajax/', add_buku_ajax, name='add_buku_ajax')
]