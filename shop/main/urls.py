from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('category/<slug:slug>', views.category_product_list, name='category_product_list'),
    path('product_detail/<slug:slug>', views.product_detail, name='product_detail'),

    path('register_page', views.register_page, name='register_page'),
    path('login_page', views.login_page, name='login_page'),
    path('logout_page', views.logout_page, name='logout_page'),

]


