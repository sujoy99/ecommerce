from django.shortcuts import render

# Create your views here.
def store(request):
    template_name = "store/store.html"
    context = {}

    return render(request, template_name, context)

def cart(request):
    template_name = "store/cart.html"
    context = {}

    return render(request, template_name, context)

def checkout(request):
    template_name = "store/checkout.html"
    context = {}

    return render(request, template_name, context)
