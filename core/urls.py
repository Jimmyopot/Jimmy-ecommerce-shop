from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('items/', views.products, name='items'),
    path('', views.HomeView.as_view(), name='home'),
    path('products/<slug:slug>/', views.ProductDetailView.as_view(), name='products'),
    path('order-summary/', views.OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug:slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug:slug>/', views.remove_from_cart, name='remove-from-cart'),
    path('remove-single-item-from-cart/<slug:slug>/', views.remove_single_item_from_cart, name='remove-single-item-from-cart'),
] 