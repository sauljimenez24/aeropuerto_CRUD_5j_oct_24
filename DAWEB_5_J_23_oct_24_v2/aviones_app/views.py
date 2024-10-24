from django.shortcuts import render
from .models import Aviones
# Create your views here.
def listadoAviones(request):
    losAviones=Aviones.objects.all()
    return render(request,"gestionarAviones.html",{"misaviones":losAviones})

