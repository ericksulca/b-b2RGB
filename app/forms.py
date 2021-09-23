from django.forms import ModelForm
from .models import *
from django import forms

class ImagenForm(ModelForm):
	class Meta:
		model = Imagen
		fields = ['descripcion', 'imagen']
		widgets = {
			'descripcion': forms.Textarea(attrs={'rows': 5,'class':'form-control'}),
			#'imagen': forms.Textarea(attrs={'rows': 5,'class':'form-control'})
		}
