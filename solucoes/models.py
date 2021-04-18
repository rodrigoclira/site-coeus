# -*- coding: utf-8 -*-
#<Autor> Rodrigo Lira (rodrigoclira@yahoo.com.br)
from django.db import models
from os import sep 

class Solucao(models.Model):
	name = models.CharField("nome", max_length=100, unique=True)
	image = models.ImageField("imagem",upload_to='images'+sep+'produtos') 
	summary = models.TextField('resumo')
	description = models.TextField('descricao')
	
	class Meta:
		verbose_name = "solução"
		verbose_name_plural = "soluções"

	def __unicode__(self):
		return self.name
