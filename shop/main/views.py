from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from .forms import CreateUserForm
from .models import *


def index(request):  # main page
    products = Product.objects.all()

    categories = Category.objects.all()

    context = {'products': products,
               'categories': categories,
               }

    return render(request, 'main/index.html', context)


def product_detail(request, slug):  # shows details about chosen product
   # product = Product.objects.get(id=pk)
    product = get_object_or_404(Product, slug=slug)

    categories = Category.objects.all()

    context = {'product': product,
               'categories': categories,
               }

    return render(request, 'main/product_detail.html', context)


def category_product_list(request, slug):  # shows products by category
    category = get_object_or_404(Category, slug=slug)

    #category = Category.objects.get(id=pk)

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


def cart(request):
    try:
        if request.user.is_authenticated:
            customer = request.user.customer
            order = Order.objects.get(customer=customer)
            items = order.orderitem_set.all()
    except Exception:
        items = []
        order = {'cart_total': 0, 'total_price': 0}

    context = {'items': items, 'order': order}

    return render(request, 'main/cart.html', context)


