#-*- coding: utf-8 -*-
from quem_somos_nos.models import Person
from django.contrib import admin

class PersonAdmin(admin.ModelAdmin):
	fieldsets = [
		("Informações pessoais", {'fields' : ['name','photo_perfil','photo1','photo2','lattes']}),
		("Informações profissionais", {'fields' :
['linkedin','responsability','email']}),
		("Outras informações", {'fields' : ['description'] 
		})
	]
	list_display = ("name","responsability")
	search_fields = ["name","responsability"]
#	list_filter = ['graduation']

admin.site.register(Person,PersonAdmin)
