from unittest import result
from django.shortcuts import render
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from matplotlib.style import context
from sympy import false
from product.formc import CheckoutForm, ContactForm
from product.models import *
from cart.models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import logout
from django import forms

from petshop.utils import *


# Create your views here.
def index_view(request):   
    data = cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']
    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request,'index.html',context)

def about_view(request):
    data = cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']
    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'about-us.html',context)

def shop_page_view(request):
    data = cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']
    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request,'shop-page.html',context)

def shop_list_view(request):
    data = cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']
    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request,'shop-list.html',context)

def cart_view(request):
    data = cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,'cart.html',context)

def cart_delete(request):
    OrderItem.objects.all().delete()
    data = cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,'cart.html',context)

def search_views(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created =Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems = order.get_cart_items
        
        data = cartData(request)
        cartItems=data['cartItems']
    else:
        items=[]
        order={'get_cart_items':0, 'get_cart_total':0}
        cartItems=order['get_cart_items']
        
    search=request.GET.get('search',False)
        
    results=Product.objects.filter(name__icontains=search)
    
    context={'results':results,'cartItems':cartItems}
    return render(request,'search.html',context)
    

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def checkout_view(request):
    data = cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']
    
    form = CheckoutForm()
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.CheckOut(email=request.user.email,request=request)
            OrderItem.objects.all().delete() 
            return HttpResponseRedirect('/') 
    
    context = {'items':items, 'order':order, 'cartItems':cartItems, 'form':form}   
    return render(request,'checkout.html',context)
    
def Logout(request):
    logout(request)
    context = {}
    return render(request,'index.html',context)


def contact_view(request):
    data = cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']
    
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.contact(email=request.user.email)
            return HttpResponseRedirect('/')
    
    context = {'items':items, 'order':order, 'cartItems':cartItems, 'form': form}
    return render(request, 'contact.html', context)


    