# -*- coding: utf-8 -*-
#<Autor> Rodrigo Lira (rodrigoclira@yahoo.com.br)
from blog.models import Post, Category, Image
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		("Postagem", {'fields' : ['title','image','description','text', 'category']}),
		
				]
	list_display = ("title", "author" ,"category", "published", "was_published_recently")
	search_fields = ["title"]
	list_filter = ['published']
	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()


class CategoryAdmin(admin.ModelAdmin):
	fieldsets = [ 
		('Informações', {'fields': ['name']})
				]
	prepolutaded_fields = {'slug': ('name',)}
	list_display = ["name"]


class Image(admin.ModelAdmin):
	fieldsets = [ ('',{'fields': ['description','image']}) ]
	search_field = ['description']
	list_display = ('description','published')

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)

