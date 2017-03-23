from __future__ import unicode_literals

from django.db import models
import uuid
from datetime import date
from dateutil.relativedelta import relativedelta

def one_month_from_now():
    return date.today() + relativedelta(months=+1)

#A product is an insurance offer, the basic block of the catalogue
class Product(models.Model):
    #Product name and description
    product_name = models.CharField(max_length=30)
    product_description = models.TextField(help_text="a simple description of the product")
    #toggle to publih / unpublish a product
    is_published = models.BooleanField(default=True, help_text="allow this product to be subscribed")
    #simple pricing scheme to start : fixed price and payout
    base_price = models.DecimalField(max_digits=6, decimal_places=2, help_text="price of the product")
    base_payout = models.DecimalField(max_digits=8, decimal_places=2, help_text="the amount to reimburse the customer if insurance is activated")
    
    def __str__(self):
        return product_name

#A quote is a contract proposal which hasn't been accepted yet by the customer
class Quote(models.Model):
    #a unique ID to reference a given quote
    id = models.UUIDField(primary_key=True, default= uuid.uuid4)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    creation_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField(null=True, blank=True)
    quote_price = models.DecimalField(max_digits=6, decimal_places=2)
    quote_payout = models.DecimalField(max_digits=8, decimal_places=2)
    QUOTE_STATUS = (
        ('p', 'Pending'),
        ('e', 'Expired'),
        ('a', 'Accepted'),
        ('r', 'Refused'),
    )
    status = models.CharField(max_length=1, choices=QUOTE_STATUS, blank=True, default='p', help_text='Quote status')

    def __str__(self):
        return "Quote %s (%s)" % (self.id, self.product)

class Contract(models.Model):
    #a unique ID to reference a given contract
    id = models.UUIDField(primary_key=True, default= uuid.uuid4)
    product =  models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    quote =  models.ForeignKey('Quote', on_delete=models.SET_NULL, null=True)
    customer_mail = models.EmailField()
    start_date = models.DateField(null=False, default=date.today)
    expiration_date = models.DateField(null=False, default=one_month_from_now)
    CONTRACT_STATUS = (
        ('n', 'Not started'),
        ('v', 'Valid'),
        ('e', 'Expired'),
        ('o', 'Void'),
        ('c', 'Claimed')
    )
    status = models.CharField(max_length=1, choices=CONTRACT_STATUS, blank=True, default='v', help_text='Contract status')
    
    def __str__(self):
        return "Contract %s (%s)" % (self.id, self.product)
