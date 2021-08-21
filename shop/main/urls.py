from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('category/<slug:slug>', views.category_product_list, name='category_product_list'),
    path('product_detail/<slug:slug>', views.product_detail, name='product_detail'),
    path('cart', views.cart, name='cart'),

    path('register', views.register_page, name='register_page'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_page, name='logout_page'),

]


