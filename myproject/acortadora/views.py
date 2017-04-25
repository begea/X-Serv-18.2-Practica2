from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from acortadora.models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def lista_paginas(request):
    if request.method == "GET":
		resp += "<form action='' method='POST'>"
		resp +=   "<input type='text' name='contenido'>"
		resp +=   "<input type='submit' value='Acortar'>"
		resp += "</form>"

        resp = "Las URLS disponibles son: "
        lista_pages = Pages.objects.all()
        for page in lista_pages:
            resp += "<br>" + page.id + " --> " + page.page
        return HttpResponse(resp)

    if request.method == "POST":
        url = request.POST['contenido']
		if url.find("http") != 0 :
			url = "http://" + url
        try:
            pagina = Pages.objects.get(page=url).id
		except :
			Pages(url=url).save()
            pagina = Pages.objects.get(page=url).id
            resp = url + "<a href='/" + str(pagina) + "'>" + str(pagina) + "</a>"
        return HttpResponse(resp)

def url_acortada(request, id):
	try :
		resp = Pages.objects.get(id=id).url
		return HttpResponseRedirect(resp)
	except :
		resp = "404 Not Found"
    return HttpResponse(resp)
