from django.contrib import admin

from .models import Product, Quote, Contract

admin.site.register(Product)
admin.site.register(Contract)

class QuoteAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date',)
    
admin.site.register(Quote, QuoteAdmin)
