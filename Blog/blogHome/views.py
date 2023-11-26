from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from .models import *


""" vista basada en funcion """
def home(request):
    if request.method == 'GET':
        template_name = 'index.html'
        # return render(request, template_name)
        data = {'user': 'jose', "id": 1, "email": "jose@gmail.com"}
        return JsonResponse(data)
    elif request.method == 'POST':
        template_name = 'formulario.html'
        return render(request, template_name)
    return render(request, '404.html')
    


class BlogWelcome(View):
    def get(self, request):
        template_name = 'blog_welcome.html'
        return render(request, template_name)
    
    def post(self, request):
        pass





class ContactoBlog(View):
    def get(self, request):
        template_name = 'formulario.html'
        return render(request, template_name)
    
    def post(self, request):
        print('datos del request:',request.POST)
        data = request.POST
        print(data['email'])
        print(data['nombre'])
        print(data['mensaje'])
        # template_name = 'gracias.html'
        # return render(request, template_name)
        return redirect('gracias')


class Gracias(View):
    def get(self, request):
        template_name = 'gracias.html'
        return render(request, template_name)


class HelloDjango(View):
    def get(self, request):
        # print(request.user)
        template_name = 'hello.html'

        data = {
            'email': 'pedro@gmail.com',
            'username': 'pedro',
            'isAdmin': True,
            'creditos': ['certificadoFrontend', 'certicadoBackend', 'certifyCloudAWS']
        }

        return render(request, template_name, data)



class HelloDjangoORM(View):
    def get(self, request):
        # print(request.user)
        template_name = 'hello.html'


        # Django el ORM genera la siguiente consulta: SELECT * FROM estudiantes;
        # articulos = ArticulosBlog.objects.all()
        # print(articulos)

        # busqueda con filtros o clausula where
        # articulos_filtro = ArticulosBlog.objects.filter(body__icontains='NUEVO')
        # print(articulos_filtro)

        # buscar u obtener productos unicos por id, etc
        # articulo = ArticulosBlog.objects.get(id='2')
        # print(articulo)


        # actualizar registros
        # articulo = ArticulosBlog.objects.get(id='1')
        # articulo.title_blog = 'Nuevo ttitulo desde el ORM'
        # articulo.body = 'nueva desc. desde orm'
        # articulo.save()



        return render(request, template_name, {})
