from django.db import models

# Create your models here.

class Imagen(models.Model):
    descripcion   = models.TextField(verbose_name=u"Descripción",blank=True,null=True)
    imagen        = models.ImageField(verbose_name=u"Fotografía",null=True,default="no-imagen.png")#upload_to='%Y/%m/%d',
    fecharegistro = models.DateTimeField(auto_now_add=True, blank=True)
    activo        = models.BooleanField(blank=True,default=True)
    
    class Meta:
        ordering = ["-fecharegistro"]
    def __str__(self):
        return str(self.fecharegistro)