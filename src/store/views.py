from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

# Create your views here.
def store(request):
    template_name = "store/store.html"

    if request.user.is_authenticated:
        customer = request.user.customer
        
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        items = order.orderitem_set.all()

        cartItems = order.get_cart_item

    else:
        items = []
        order = {
            'get_cart_item' : 0,
            'get_cart_total' : 0,
            'shipping' : False
        }
        cartItems = order['get_cart_item']
    
    products = Product.objects.all()
    context = {
        
        'products' : products,
        'cartItems' : cartItems
    }

    return render(request, template_name, context)

def cart(request):
    template_name = "store/cart.html"
    
    if request.user.is_authenticated:
        customer = request.user.customer
        
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        items = order.orderitem_set.all()

        cartItems = order.get_cart_item

    else:
        items = []
        order = {
            'get_cart_item' : 0,
            'get_cart_total' : 0,
            'shipping' : 'False'
        }
        cartItems = order['get_cart_item']

    context = {
        'items' : items,
        'order' : order,
        'cartItems' : cartItems
    }

    return render(request, template_name, context)

def checkout(request):
    template_name = "store/checkout.html"
    
    if request.user.is_authenticated:
        customer = request.user.customer
        
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        items = order.orderitem_set.all()

        cartItems = order.get_cart_item

    else:
        items = []
        order = {
            'get_cart_item' : 0,
            'get_cart_total' : 0,
            'shipping' : 'False'
        }
        cartItems = order['get_cart_item']

    context = {
        'items' : items,
        'order' : order,
        'cartItems' : cartItems
    }

    return render(request, template_name, context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('productId:', productId)
    print('action:', action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    # condition for add or remove
    if action == 'add':
        orderItem.quantity = orderItem.quantity +1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity -1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)