from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
from .forms import CursoFormulario
from .models import Curso

def inicio_view(request):
    return render(request, "AppCoder/inicio.html")

def cursos_view(request):
    if request.method == "GET":
        form = CursoFormulario()
        return render(
            request,
            "AppCoder/curso_formulario_avanzado.html",
            context={"form": form}
        )
    else:
        formulario = CursoFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            mi_curso = Curso(curso=request.POST["curso"], camada=request.POST["camada"])
            mi_curso.save()
        return redirect("AppCoder:inicio")

def profesores_view(request):
    return render(request, "AppCoder/padre.html")

def videojuegos_view(request):
    return render(request, "AppCoder/videojuegos.html")