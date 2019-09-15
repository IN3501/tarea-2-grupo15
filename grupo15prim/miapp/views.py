from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'home.html')
def reserva(request):
	return render(request, 'reserva.html')
def envioexitoso(request):
	return render(request, 'envioexitoso.html')