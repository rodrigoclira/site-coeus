from django.db import models
from os import sep


class Slider(models.Model):
	name = models.CharField('nome', max_length=30)

	def __unicode__(self):
		return ("%s" % self.name)

class Slide(models.Model):
	name = models.CharField('nome', max_length=50)
	image = models.ImageField("imagem", upload_to ='images'+ sep +'home'+ sep +'slide')
	subtitle = models.CharField("legenda", max_length=80,blank=True)
	link = models.CharField('link', max_length=50)
	slider = models.ForeignKey(Slider)
	
	def __unicode__(self):
		return ("%s" % self.name)

