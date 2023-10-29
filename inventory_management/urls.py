from django.urls import path
from inventory_management.views import admin_page, register, login_admin, logout_user, add_buku_ajax
from inventory_management.views import get_product_json, delete_buku, error_login

app_name = 'inventory_management'

urlpatterns = [
    path('literaloka-admin/', admin_page, name='literaloka_admin'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('add-buku-ajax/', add_buku_ajax, name='add_buku_ajax'),
    path('delete-buku/<int:id>/', delete_buku, name='delete_buku'),
    path('login-as-admin/', login_admin, name='login_admin'),
    path('404-not-found/', error_login,name='page_eror')
]