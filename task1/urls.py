from django.urls import path

from . import views

app_name = 'task1'

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop_cart/', views.shop_cart, name='shop_cart'),
    path('django_auth/', views.sign_up_by_django, name='django_auth'),
]
