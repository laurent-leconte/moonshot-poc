from django.conf.urls import url

from . import views


urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^products/$', views.ProductListView.as_view(), name='products'),
     url(r'^products/(?P<pk>[-\w]+)/quote/$', views.get_quote, name='get_quote'),
     
]