from django.shortcuts import render

# Create your views here.

from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from .models import *
from .forms import *

def Home(request):
	if request.method=='GET':
		form = ImagenForm()
		return render(request,'base.html',{'form':form})
	if request.method=='POST':
		pass
		return render(request,'base.html',{'form':form})