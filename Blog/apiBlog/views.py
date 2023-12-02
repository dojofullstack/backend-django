from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions
# from django.contrib.auth.models import User
from blogHome.models import ArticulosBlog
from .serializers import ArticulosBlogSerializer



""" API CRUD para el Blog """
# C - CREATE
# R - READ
# U - UPDATE
# D - DELETE
class ApiCRUDBlog(APIView):
    
    def get(self, request, articulo=None):
        
        
        # articulosSerializer = []
        # for item in articulos:
            # itemJSON = {
            #     'titulo': item.title_blog,
            #     'slug': item.articule_url,
            #     'body': item.body,
            #     'dataCreated': item.data_create,
            # }
            # articulosSerializer.append(itemJSON)
        # articulosSerializer = [{
        #     'titulo': item.title_blog,
        #     'slug': item.articule_url,
        #     'body': item.body,
        #     'dataCreated': item.data_create,
        # } for item in articulos]

        """si vas a relizar un array ORM o conjunto de registros
            con all() o filter() debes
            indicar el paramentro many=True
        """

        if articulo:
            articulo = ArticulosBlog.objects.get(id=articulo)
            serial = ArticulosBlogSerializer(articulo)
        else:        
            articulos = ArticulosBlog.objects.all().order_by('data_create')
            
            # implemnetar paginacion 10 registro por pagina
            # Implementar filtros de busqueda, por fields

            serial = ArticulosBlogSerializer(articulos, many=True)


        # print('articulos', articulos)
        return Response(serial.data)
    