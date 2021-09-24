from django.shortcuts import render

# Create your views here.

from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from .models import *
from .forms import *
import os 

def Home(request):
	if request.method=='GET':
		form = ImagenForm()
		return render(request,'base.html',{'form':form})
	if request.method=='POST':
		Datos = request.POST
		form = ImagenForm(request.POST, request.FILES)
		if form.is_valid():
			oImagen = Imagen()
			oImagen.descripcion = Datos["descripcion"]
			oImagen.save()
			oImagen.imagen = form.cleaned_data["imagen"]
			oImagen.save()
			#try:
			ruta_imagen = '.'+str(oImagen.imagen.url)
			img_bgr = cv2.imread(ruta_imagen, cv2.IMREAD_UNCHANGED)
			#img_bgr = cv2.imread('/home/erick/Software/B&B2Color/convert2color/foto.jpeg')
			if img_bgr.ndim == 2:
				img_color = cv2.cvtColor(img_bgr, cv2.COLOR_GRAY2BGR)  #G
				print("Entro en gris")
			else:
				print("Entro en BGR")
				img_color = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB) #RGB
			cv2.imwrite('media/color.jpeg',img_color)
			oImagen.save()
			

		return render(request,'base.html',{'form':form, 'oImagen':oImagen})