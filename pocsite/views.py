from django.shortcuts import render
from django.views import generic
from .models import Product
from .services import generate_quote
from django.core.exceptions import PermissionDenied

def index(request):
    published_product_list = Product.objects.filter(is_published=True)
    products = [str(p) for p in published_product_list]
    return render(request, 'index.html', context={'products':products})
    
def get_quote(request, pk):
    quote = generate_quote(pk)
    if quote is not None:
        return render(request, 'quote.html', context={'quote':quote})
    raise PermissionDenied

class ProductListView(generic.ListView):
    model = Product
    def get_queryset(self):
        return Product.objects.filter(is_published=True)