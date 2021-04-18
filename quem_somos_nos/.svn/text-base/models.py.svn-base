# -*- coding: utf-8 -*-
#<Autor> Rodrigo Lira (rodrigoclira@yahoo.com.br)
from django.db import models
from coeus.settings import MEDIA_ROOT
from os import sep


class Person(models.Model):
	name = models.CharField("nome", max_length=100, unique=True) #Nome e sobre nome
	description = models.TextField("descrição") #Breve descrição
	photo1 = models.ImageField("foto da animação 1", upload_to ='images'+ sep + 'pessoas') 
	photo2 = models.ImageField("foto da animação 2", upload_to ='images'+ sep + 'pessoas')
	photo_perfil = models.ImageField("foto do perfil", upload_to ='images'+ sep + 'pessoas')
	linkedin = models.URLField(verify_exists = True, blank=True) #url de linkedin (ver a história profissional)
	lattes = models.URLField(verify_exists = True, blank=True)
	responsability = models.CharField("cargo", max_length=100) # Cargo exercido na empresa
	email = models.EmailField()

	class Meta:
		verbose_name = "Pessoa"
		verbose_name_plural = "Pessoas"

	def __unicode__(self):
		return self.name


