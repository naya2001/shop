from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about_us', views.about_us, name='about_us'),
    path('contacts', views.contacts, name='contacts'),

    path('category/<slug:slug>', views.category_product_list, name='category_product_list'),
    path('product_detail/<slug:slug>', views.product_detail, name='product_detail'),
    path('cart', views.cart, name='cart'),
    path('message', views.order_is_confirmed, name='order_is_confirmed'),

    path('update_item/', views.update_item, name='update_item'),
    path('profile', views.profile_page, name='user_page'),

    path('register', views.register_page, name='register_page'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_page, name='logout_page'),

]


