from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ShopIndex'),
    path('about/', views.about, name='ShopAbout'),
    path('contact/', views.contact, name='ShopContact'),
    path('tracker/', views.tracker, name='ShopTracker'),
    path('search/', views.search, name='ShopSearch'),
    path('productView/', views.productView, name='ShopProductView'),
    path('checkout/', views.checkout, name='ShopCheckout'),
]