from django.urls import path
from django.urls import include, re_path
from .views import *
from .form import *


urlpatterns = [
    
    path('', index, name="index"),
    path('display_laptop', display_laptops, name="display_laptop"),
    path('display_desktop', display_desktops, name="display_desktop"),
    path('display_mobile', display_mobiles, name="display_mobile"),
    
    path('add_laptop', add_laptop, name="add_laptop"),
    path('add_desktop', add_laptop, name="add_desktop"),
    path('add_mobile', add_laptop, name="add_mobile"),
    
    path('edit_laptop/<pk>', edit_laptop, name='edit_laptop'),
    path('edit_desktop/<pk>', edit_desktop, name='edit_desktop'),
    path('edit_mobile/<pk>', edit_mobile, name='edit_mobile'),
    
    path('delete_laptop/<pk>', delete_laptop, name='delete_laptop'),
    path('delete_desktop/<pk>', delete_desktop, name='delete_desktop'),
    path('delete_mobile/<pk>', delete_mobile, name='delete_mobile'),
    
]