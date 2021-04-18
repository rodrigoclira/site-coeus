#-*- coding: utf-8 -*-
from home.models import Slider, Slide
from django.contrib import admin

class SlideInLine(admin.TabularInline):
	model = Slide
	extra = 3


class SliderAdmin(admin.ModelAdmin):
	list_display = ("name",)


class SlideAdmin(admin.ModelAdmin):
	fieldsets = [
		("Informações", {'fields' : ['name','image','subtitle','link', 'slider']}),
				]
	list_display = ("name", "slider", "link")
	search_fields = ["name"]
	list_filter = ['slider']

admin.site.register(Slide, SlideAdmin)
