# from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('articulos', ApiCRUDBlog.as_view(), name='articulos'),
    path('articulo/<int:articulo>', ApiCRUDBlog.as_view(), name='articulo'),
]



# <articulo: slug>