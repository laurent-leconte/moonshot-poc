from django.shortcuts import render
from .models import Product

def index(request):
    published_product_list = Product.objects.filter(is_published=True)
    products = [str(p) for p in published_product_list]
    return render(request, 'index.html', context={'products':products})
