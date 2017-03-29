from django.conf.urls import url

from . import views


urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^products/$', views.ProductListView.as_view(), name='products'),
     
]