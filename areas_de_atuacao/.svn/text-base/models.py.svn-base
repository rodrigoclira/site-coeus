# -*- coding: utf-8 -*-
#<Autor> Rodrigo Lira (rodrigoclira@yahoo.com.br)
from django.db import models
from os import sep 

class Area(models.Model):
	name = models.CharField("nome", max_length=100, unique=True)
	#image = models.ImageField("imagem",upload_to='images'+sep+'areas') 
	icon = models.CharField("ícone",max_length=50)
	description = models.TextField('descricao')

	def __unicode__(self):
		return u"%s" % self.name

	class Meta:
		verbose_name = "área de atuação"
		verbose_name_plural = "áreas de atuação"
