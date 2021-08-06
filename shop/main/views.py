from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from .forms import CreateUserForm, CategoryForm, ProductsForm
from .models import Category, Product


def index(request):
    products = Product.objects.all()

    categories = Category.objects.all()

    context = {'products': products,
               'categories': categories,
               }

    return render(request, 'main/index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)

    categories = Category.objects.all()

    context = {'product': product,
               'categories': categories,
               }

    return render(request, 'main/product_detail.html', context)


def store(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'main/store.html', context)


def category_product_list(request, pk):

    category = Category.objects.get(id=pk)

    categories = Category.objects.all()

    context = {'category': category,
               'categories': categories
               }

    return render(request, 'main/category_product_list.html', context)


def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'main/user_templates/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}

        return render(request, 'main/user_templates/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login_page')


def show_categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'main/category_templates/show_categories.html', context)


def add_category(request):

    form = CategoryForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'main/category_templates/category_form.html', context)


def update_category(request, pk):

    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('show_categories')

    context = {'form': form}

    return render(request, 'main/category_templates/category_form.html', context)


def delete_category(request, pk):

    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('show_categories')

    context = {'item': category}

    return render(request, 'main/category_templates/category_delete_form.html', context)


def show_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'main/product_templates/show_products.html', context)


def add_product(request):

    form = ProductsForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'main/product_templates/product_form.html', context)


def update_product(request, pk):

    product = Product.objects.get(id=pk)
    form = ProductsForm(instance=product)

    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('show_products')

    context = {'form': form}

    return render(request, 'main/product_templates/product_form.html', context)


def delete_product(request, pk):

    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('show_products')

    context = {'item': product}

    return render(request, 'main/product_templates/product_delete_form.html', context)


