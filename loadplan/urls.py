from django.urls import path
from . import views

urlpatterns = [
    path('', views.loadplan, name='loadplan'),
    path('orderdetails', views.orderdetails, name='orderdetails'),
    path('availablecapacity', views.availablecapacity, name='availablecapacity'),
    path('capreqd', views.capreqd, name='capreqd'),
    path('ordtable', views.ordtable, name='ordtable'),
    path('avctable', views.avctable, name='avctable'),
    path('cprtable', views.cprtable, name='cprtable')

]