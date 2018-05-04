"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from firstapp import views
from django.urls import re_path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^$|home/', views.index),
    #path('', views.index, name='home'),

    path('about/', TemplateView.as_view(template_name="about.html",
                                        extra_context={"header": "О сайте"})),
    path('contact/', TemplateView.as_view(template_name="contact.html")),

    #re_path(r'^users/$', views.users),
    #re_path(r'^about', views.about),
    #re_path(r'^products/(?P<productid>\d+)/', views.products),
    #re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),

    #products page
    path('products/<int:productid>/', views.products),
    path('products/', views.products),

    #users page
    path('users/<int:id>/<name>/', views.users),
    path('users/', views.users),
]