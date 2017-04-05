from .models import Quote, Product, Contract

def generate_quote(product_id):
    try:
        #IRL this would call an API or third-party service
        product = Product.objects.get(id=product_id)
        if product.is_published:
            quote = Quote.objects.create(product=product, quote_price=product.base_price,
             quote_payout=product.base_payout,status='p')
            return quote
        else:
            #TODO : handle non-published products properly
            print("non-published product")
            return None
    except Product.DoesNotExist:
        #TODO : handle error properly
        print("non-existent product")
        return None