#-*- coding: utf-8 -*-
from solucoes.models import Solucao
from django.contrib import admin

class SolucaoAdmin(admin.ModelAdmin):
	fieldsets = [
		("Informações", {'fields' : ['name','image','summary','description']}),
	]
	list_display = ("name",)
	search_fields = ["name"]

admin.site.register(Solucao,SolucaoAdmin)


