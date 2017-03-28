from django.shortcuts import render
from .models import Product

def index(request):
    published_product_list = Product.objects.filter(is_published=True)
    return render(request, 'index.html', context={})
