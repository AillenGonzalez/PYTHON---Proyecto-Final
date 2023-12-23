from django.urls import path
from AppCoder.views import cursos_view, inicio_view, profesores_view

app_name = "AppCoder"

urlpatterns = [
    path("cursos/", cursos_view, name="cursos"),
    path("profesores/", profesores_view),
    path("inicio/", inicio_view, name="inicio"),
]
