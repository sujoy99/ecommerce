from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

# Create your views here.
def store(request):
    template_name = "store/store.html"
    products = Product.objects.all()
    context = {
        
        'products' : products
    }

    return render(request, template_name, context)

def cart(request):
    template_name = "store/cart.html"
    
    if request.user.is_authenticated:
        customer = request.user.customer
        
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        items = order.orderitem_set.all()

    else:
        items = []
        order = {
            'get_cart_item' : 0,
            'get_cart_total' : 0
        }

    context = {
        'items' : items,
        'order' : order
    }

    return render(request, template_name, context)

def checkout(request):
    template_name = "store/checkout.html"
    
    if request.user.is_authenticated:
        customer = request.user.customer
        
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        items = order.orderitem_set.all()

    else:
        items = []
        order = {
            'get_cart_item' : 0,
            'get_cart_total' : 0
        }

    context = {
        'items' : items,
        'order' : order
    }

    return render(request, template_name, context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('productId:', productId)
    print('action:', action)

    return JsonResponse('Item was added', safe=False)