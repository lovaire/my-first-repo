from django.urls import path
from main.views import show_main, add_money, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_item, delete, get_product_json, add_money_ajax, delete_by_ajax
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-money', add_money, name='add_money'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('delete/<int:id>/', delete, name='delete'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('add-money-ajax/', add_money_ajax, name='add_money_ajax'),
    path('delete-by-ajax/', delete_by_ajax, name='delete_by_ajax'),
]
