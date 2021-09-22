from .models import Category, Product, Customer

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['address', 'phone']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_title']


class ProductsForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


