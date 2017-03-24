from django.http import Http404
from django.shortcuts import render
from .models import  Solicitud, Coordinador

def index(request):
    solicitudes = Solicitud.objects.all()
    coordinador = Coordinador.objects.all()

    return render(request, 'poda/index.html', {'solicitudes': solicitudes})

def detail(request, id_solicitud):
    #return HttpResponse("<h2>Detalle de la solicitud:" + str(id_solicitud) + "</h2>")
    try:
        solicitud = Solicitud.objects.get(pk=id_solicitud)
        #coordinador = Coordinador.objects.get(id=id_coordinador)
    except Solicitud.DoesNotExist:
        raise Http404("La solicitud no existe")
    return render(request, 'poda/detail.html', {'solicitud': solicitud})