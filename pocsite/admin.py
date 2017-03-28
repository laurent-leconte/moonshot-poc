from django.contrib import admin

from .models import Product, Quote, Contract


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'is_published', 'base_price', 'base_payout')
    fields = ['product_name', 'product_description', 'is_published', ('base_price', 'base_payout')]

class QuoteAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date',)

class ContractAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Contract, ContractAdmin)    
admin.site.register(Quote, QuoteAdmin)
