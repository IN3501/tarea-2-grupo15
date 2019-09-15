from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'home.html')
def reserva(request):
	return render(request, 'reserva.html')
def recuperar(request):
	texto=request.POST["inputText"]
	numero=request.POST["inputNumber"]
	correo=request.POST["inputEmail"]
	carrera=request.POST["input Select"]
    
	diccionario={}
	diccionario["comentario"]=texto 
	diccionario["comentario2"]=numero
	diccionario["comentario3"]=correo
	diccionario["comentario4"]=carrera

	return render(request, "envio.html", diccionario)
def registro(request):
	return render(request, 'registro.html')