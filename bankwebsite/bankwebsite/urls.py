"""
URL configuration for bankwebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
from bankwebsite.views import index
from bankwebsite.views import next_page
from bankwebsite.views import register
from bankwebsite.views import last_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('nextpage.html/', views.next_page, name='next_page'),
    path('register.html/', views.register, name='register'),
    path('lastpage.html/', views.last_page, name='last_page'),
]
