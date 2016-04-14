from django.shortcuts import render
from models import Pages
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def cms(request, recurso):
    if request.user.is_authenticated():
        estado = "<br><br>Hola " + request.user.username +\
                ". <a href='/admin/logout/'>Logout</a><br>"
    else:
        estado = "<br><br>No estas registrado. <a href='/admin/login/'>Login</a><br>"

    if request.method == "GET":
        try:
    		contenido = Pages.objects.get(name=recurso)
    		return HttpResponse(contenido.name+ ':' + contenido.page)
    	except Pages.DoesNotExist:
    		return HttpResponseNotFound("Recurso no encontrado: " + recurso)

    elif request.method == "PUT":
        if request.user.is_authenticated():
            pagina = Pages(name=recurso, page=request.body)
            pagina.save()
            return HttpResponse("Pagina guardada: "+ request.body)
        else:
            return HttpResponse("no se puede anadir la pagina")
    else:
        return HttpResponse( "metodo no disponible")

    return HttpResponseNotFound(estado)
