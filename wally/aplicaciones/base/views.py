import random
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post,Categoria,RedesSociales,Web
from .utils import *




class Inicio(ListView):

    def get(self,request,*args,**kwargs):
        posts = list(Post.objects.filter(
                estado = True,
                publicado = True
                ).values_list('id',flat = True))
        principal = random.choice(posts)
        posts.remove(principal)
        principal = consulta(principal)

        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)
        post4 = random.choice(posts)
        posts.remove(post4)

        try:
            post_videojuegos = Post.objects.filter(
                                estado = True,
                                publicado = True,
                                categoria = Categoria.objects.get(nombre = 'Videojuegos')
                                ).latest('fecha_publicacion')
        except:
            post_videojuegos = None

        try:
            post_general = Post.objects.filter(
                            estado = True,
                            publicado = True,
                            categoria = Categoria.objects.get(nombre = 'General')
                            ).latest('fecha_publicacion')
        except:
            post_general = None
        
        

        contexto = {
            'principal':principal,
            'post1': consulta(post1),
            'post2': consulta(post2),
            'post3': consulta(post3),
            'post4': consulta(post4),
            'post_general':post_general,
            'post_videojuegos':post_videojuegos,
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),

        }
        return render(request,'index.html',contexto)

class Listado(ListView):

 def get(self,request,nombre_categoria,*args,**kwargs):
        contexto = generarCategoria(request,nombre_categoria)
        return render(request,'categoria.html',contexto)





        


