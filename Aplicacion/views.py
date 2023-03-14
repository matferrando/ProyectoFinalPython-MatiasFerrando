from django.shortcuts import render
from django.http import HttpResponse

def saludo (request):
    return HttpResponse("Hola Django - Coder")

def saludo_a (request, nombre):
    return HttpResponse(f"Hola Como estas {nombre.capitalize()}")

def mostrar_mi_template(request):
    context = {
        "nombre": "Matias",
        "apellido": "Ferrando"
    }

    return render(request, "Aplicacion/index.html", context)

