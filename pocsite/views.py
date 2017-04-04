from django.shortcuts import render
from django.views import generic
from .models import Product

def index(request):
    published_product_list = Product.objects.filter(is_published=True)
    products = [str(p) for p in published_product_list]
    return render(request, 'index.html', context={'products':products})
    
def get_quote(request):
    pass

class ProductListView(generic.ListView):
    model = Product
    def get_queryset(self):
        return Product.objects.filter(is_published=True)