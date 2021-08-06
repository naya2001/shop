from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('category/<str:pk>/', views.category_product_list, name='category_product_list'),
    path('product_detail/<str:pk>', views.product_detail, name='product_detail'),

    path('register_page', views.register_page, name='register_page'),
    path('login_page', views.login_page, name='login_page'),
    path('logout_page', views.logout_page, name='logout_page'),

    path('show_categories/', views.show_categories, name='show_categories'),
    path('add_category/', views.add_category, name='add_category'),
    path('update_category/<str:pk>/', views.update_category, name='update_category'),
    path('delete_category/<str:pk>/', views.delete_category, name='delete_category'),

    path('show_products/', views.show_products, name='show_products'),
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/<str:pk>/', views.update_product, name='update_product'),
    path('delete_product/<str:pk>/', views.delete_product, name='delete_product'),

]


