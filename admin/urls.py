from django.urls import path
from main.views import show_main, create_product, register, login_user, logout_user
from main.views import show_xml, show_json, show_xml_by_id, show_json_by_id 




app_name = 'admin'

urlpatterns = [
    path('', show_main, name='admin:show_main'),
    path('create-product', create_product, name='admin:create_product'),
    path('xml/', show_xml, name='admin:show_xml'),
    path('json/', show_json, name='admin:show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='admin:show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='admin:show_json_by_id'), 
    path('register/', register, name='admin:register'),
    path('login/', login_user, name='admin:login'),
    path('logout/', logout_user, name='admin:logout'),
    
]