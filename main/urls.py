from django.urls import path
from main.views import show_main, create_product, register, login_user, logout_user
from main.views import show_json

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('main/', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),   
    path('json/', show_json, name='show_json'),
]