from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.home, name='home_html'), # Redirect or handle legacy link
    path('about.html', views.about, name='about'),
    path('menu.html', views.menu, name='menu'),
    path('news.html', views.news, name='news'),
    path('contact.html', views.contact, name='contact'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/success/<int:order_id>/', views.checkout_success, name='checkout_success'),
]
