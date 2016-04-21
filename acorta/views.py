from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from models import url_reales
import urllib
from django.template import loader, Context

# Create your views here.
@csrf_exempt
def principal(request):
    lista_urls = url_reales.objects.all()
    respuesta = '<ul>'
    for url in lista_urls:
        url_corta = '/' + str(url.id)
        respuesta += '<li><a href="' + url.url_larga + '">' +  url.url_larga + '</a> '
        respuesta += '<a href="' + url_corta + '">' +  'localhost:8000' + url_corta + '</a>'
    respuesta += '</ul>'
    template = loader.get_template("plantilla.html")
    contexto = {'lista': respuesta}
    return HttpResponse(template.render(Context(contexto)))

@csrf_exempt
def post(request):
    qs = request.POST.get('url')
    try:
        url = urllib.unquote(qs).decode('utf8')
    except AttributeError:
        respuesta = "Tienes que introducir contenido en el formulario"
        return HttpResponse(respuesta)
    if url[0:6] == 'http://' or url[0:7] == 'https://':
        pass
    else:
        url = 'http://' + url
    try:
        url_found = url_reales.objects.get(url_larga = str(url))
    except url_reales.DoesNotExist:
        url_nueva = url_reales(url_larga = url)
        url_nueva.save()
        respuesta = "Url nueva introducida <br>"
        respuesta += '<a href='" "+ str(url_nueva) + '>Ve a la pagina que querias </a><br>'
        respuesta += '<a href="/"> Ve al inicio</a>'
        return HttpResponse(respuesta)
        #anadir respuesta
    #anadir pagina de respuesta, me redirige a la pagina de la url_found
    url_corta =  '/' + str(url_found.id)
    respuesta = '<a href="' + url_found.url_larga + '">'+ url_found.url_larga + '</a>'
    respuesta += '<br>'
    respuesta += '<a href="' + url_corta + '"> ' + url_corta + '</a>'
    return HttpResponse(respuesta)


def cortas(request, numero):
    try:
        found = url_reales.objects.get(id = numero)
    except url_reales.DoesNotExist:
        respuesta = "No existe esa url"
        return HttpResponse(respuesta)
    respuesta =  found.url_larga
    return HttpResponseRedirect(respuesta)
