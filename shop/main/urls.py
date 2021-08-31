from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('category/<slug:slug>', views.category_product_list, name='category_product_list'),
    path('product_detail/<slug:slug>', views.product_detail, name='product_detail'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),

    path('update_item/', views.update_item, name='update_item'),
    path('user_page', views.user_page, name='user_page'),

    path('register', views.register_page, name='register_page'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_page, name='logout_page'),

]


