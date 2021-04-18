#-*- coding: utf-8 -*-
from areas_de_atuacao.models import Area
from django.contrib import admin

class AreaAdmin(admin.ModelAdmin):
	fieldsets = [
		("Informações", {'fields' : ['name','icon','description']}),
	]
	list_display = ("name",)
	search_fields = ["name"]

admin.site.register(Area,AreaAdmin)
