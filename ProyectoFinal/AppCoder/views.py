from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

def inicio_view(request):
    return render(request, "AppCoder/inicio.html")

def cursos_view(request):
    if request.method == "GET":
        print("+" * 90)
        print("+" * 90)
        return render(
            request,
            "AppCoder/curso_formulario_basico.html",
        )
    else:
        print("*" * 90)
        print(request.POST)
        print("*" * 90)
        return render(
            request,
            "AppCoder/curso_formulario_basico.html"
        )

def profesores_view(request):
    return render(request, "AppCoder/padre.html")