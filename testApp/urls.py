from django.contrib import admin
from django.urls import path
from menu_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu_page, name='menu'),
    path('home/', views.menu_page, name='home'),
    path('shop/', views.menu_page, name='shop'),
    path('help/', views.menu_page, name='help'),
    path('nothing/', views.menu_page, name='nothing'),
    path('catalog/', views.menu_page, name='catalog'),
    path('hm/', views.menu_page, name='hm'),
]
