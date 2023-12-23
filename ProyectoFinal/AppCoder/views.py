from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

def inicio_view(xx):
    return HttpResponse("Bienvenidos")

def xx_cursos_view(xx):
#    return HttpResponse("Aquí voy a mostrar mis cursos")
    return render(xx, "AppCoder/padre.html")

def cursos_view(xx):
    nombre = "Aillen Estefania"
    apellido = "Gonzalez"
    ahora = datetime.now()

    diccionario = {
        'nombre': nombre,
        'apellido': apellido,
        'hora': ahora,
        'ciudades_preferidas': ["Buenos Aires", "Sao Pablo", "Londres"]
        } #Para enviar el contexto

    ruta = "C:\\Users\\Kida\\Documents\\Proyecto final\\ProyectoFinal\\AppCoder\\templates\\AppCoder\\padre.html"

    mi_archivo = open(ruta, "r")

    plantilla = Template(mi_archivo.read()) # Se carga en memoria nuestro documento
    contexto = Context(diccionario) # Le doy al contexto mi nombre y apellido
    documento = plantilla.render(contexto) # Acá renderizamos la plantilla en documento

    return HttpResponse(documento)

def profesores_view(xx):
    return render(xx, "AppCoder/padre.html")