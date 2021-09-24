from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string

from .forms import *
from .models import *


def index(request):  # main page
    products = Product.objects.all()

    categories = Category.objects.all()

    context = {'products': products,
               'categories': categories,
               }

    return render(request, 'main/index.html', context)


def about_us(request):
    context = {}
    return render(request, 'main/about_us.html', context)


def contacts(request):
    context = {}
    return render(request, 'main/contacts.html', context)


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


'''
def _get_form(request, formcls, prefix):
    data = request.POST if prefix in request.POST else None
    return formcls(data, prefix=prefix)
'''


def profile_page(request):
    categories = Category.objects.all()

    form = CustomerForm()
    user_form = UserForm()

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomerForm(request.POST, prefix='form')
            address = request.POST.get('address')
            phone = request.POST.get('phone')

            user_form = UserForm(request.POST, prefix='user_form')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')

            if Customer.objects.filter(user=request.user).exists():
                customer = Customer.objects.filter(user=request.user).update(address=address, phone=phone)
                user = User.objects.filter(pk=request.user.pk).update(first_name=first_name, last_name=last_name)
            else:
                customer = Customer.objects.get_or_create(user=request.user, address=address, phone=phone)

           # if form.is_valid() and user_form.is_valid():
            #    form.save()

        context = {'form': form, 'user_form': user_form, 'categories': categories, 'user': request.user}

        return render(request, 'main/user_templates/profile.html', context)
    else:
        return redirect('/login')


def cart(request):
    form = OrderForm()
    items = []
    order = {'cart_total': 0, 'total_price': 0}  # if user's order is empty

    if request.user.is_authenticated:
        customer = Customer.objects.get_or_create(user=request.user)[0]  # creating customer as logged in user

        if Order.objects.filter(customer=customer).exists():  # if orders exist, get last order
            order = Order.objects.get(customer=customer).last()
            if order.is_complete:  # if last order is completed? create new order
                order = Order.objects.create(customer=customer)
                print(order)
        else:
            order = Order.objects.get_or_create(customer=customer)[-1]  # else create new order
            print(order)

        items = order.orderitem_set.all()

       # if Order.objects.filter(customer=customer, is_complete=True).exists():  # if
        #    order = Order.objects.create(customer=customer)

    if request.method == 'POST':
            form = OrderForm(request.POST)
            order = Order.objects.filter(customer=customer).update(is_complete=True)  # set True to complete order
            return redirect('home')



    context = {'form': form, 'items': items, 'order': order}

    return render(request, 'main/cart.html', context)


def checkout(request):
    return render(request, 'main/checkout.html')


@csrf_exempt
def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    amount = data['amount']

    customer = request.user.customer

    if action == 'add':

        if not Customer.objects.filter(user=request.user).exists():  # if customer does not exist
            customer = Customer.objects.get_or_create(user=request.user)

        product = Product.objects.get(id=productId)
        order = Order.objects.get_or_create(customer=customer)[0]

        if OrderItem.objects.filter(order=order, product=product).exists():  # if the same orderItem exist
            pass
        else:
            orderItem = OrderItem.objects.get_or_create(order=order, product=product, amount=amount)  # new orderItem

    return JsonResponse('Item was added', safe=False)

