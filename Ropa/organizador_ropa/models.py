from django.db import models

choice_tipo =(
		('camisa','Camisa'),
		('pantalones','Pantalones'),
		('zapatos'',Zapatos'),
		('franela','Franela'),

	)
# Create your models here.
class RopaModels(models.Model):
	titulo = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=100)
	#tipo = models.CharField(max_length=15, choice=choice_tipo)
	marca = models.CharField(max_length=50, null=True, blank=True)