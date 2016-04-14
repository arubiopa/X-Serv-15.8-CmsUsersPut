from django.shortcuts import render
from models import Pages
<<<<<<< HEAD
from django.http import HttpResponse,HttpResponseNotFound
=======
from django.http import HttpResponse
>>>>>>> c11044086957a0f7b533510daa2e893bc98adcbb
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def cms(request, recurso):
    if request.user.is_authenticated():
        estado = "<br><br>Hola " + request.user.username +\
                ". <a href='/admin/logout/'>Logout</a><br>"
    else:
        estado = "<br><br>No estas registrado. <a href='/admin/login/'>Login</a><br>"
<<<<<<< HEAD

=======
>>>>>>> c11044086957a0f7b533510daa2e893bc98adcbb
    if request.method == "GET":
        try:
    		contenido = Pages.objects.get(name=recurso)
    		return HttpResponse(contenido.name+ ':' + contenido.page)
    	except Pages.DoesNotExist:
<<<<<<< HEAD
    		return HttpResponseNotFound("Recurso no encontrado: " + recurso)
=======
    		return HttpResponse("Recurso no encontrado: " + recurso)
>>>>>>> c11044086957a0f7b533510daa2e893bc98adcbb

    elif request.method == "PUT":
        if request.user.is_authenticated():
            pagina = Pages(name=recurso, page=request.body)
            pagina.save()
            return HttpResponse("Pagina guardada: "+ request.body)
        else:
<<<<<<< HEAD
            return HttpResponse("no se puede anadir la pagina")
    else:
        return HttpResponse( "metodo no disponible")

    return HttpResponseNotFound(estado)
=======
            return HttpResponse("no se puede añadir la pagina")
    else:
        return HttpResponse( "metodo no disponible")
    return HttpResponse(estado)
>>>>>>> c11044086957a0f7b533510daa2e893bc98adcbb
