from django.contrib import admin
from django.urls import path
from web.views import index, about, homepage

urlpatterns = [
    path('home/', index, name='home'),
    path('about/', about, name='about'),
    path('homepage/', about, name='homepage'),
    path('admin/', admin.site.urls)
    ]
