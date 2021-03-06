"""justgetit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('loadplan.urls')),
    path('orderdetails/',include('loadplan.urls')),
    path('availablecapacity/',include('loadplan.urls')),
    path('capreqd/', include('loadplan.urls')),
    path('ordtable/', include('loadplan.urls')),
    path('avctable/', include('loadplan.urls')),
    path('cprtable/', include('loadplan.urls')),
    path('material/', include('loadplan.urls')),
    path('mattable/', include('loadplan.urls')),
    path('loadsugg/', include('loadplan.urls')),
    path('exp/', include('loadplan.urls')),
    path('lg/', include('loadplan.urls')),
    path('linetable/', include('loadplan.urls')),
    path('exptable/', include('loadplan.urls')),
    path('admin/', admin.site.urls),
]
