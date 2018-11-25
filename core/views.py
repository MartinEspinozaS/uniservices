from django.shortcuts import render
from .models import Image

def home_page(request):
    images = Image.objects.order_by('?').first()
    return render(request, 'core/home_page.html', {'images' : images})
    
def lista_servicios(request):
    return render(request, 'core/lista_servicios.html' )

def infoservice(request):
	return render(request, 'core/infoservice.html')

def lista_campus(request):
	return render(request, 'core/lista_campus.html')

def lista_departamento(request):
	return render(request, 'core/lista_departamento.html')

   