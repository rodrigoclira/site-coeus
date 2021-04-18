# -*- coding: utf-8 -*-
#<Autor> Rodrigo Lira (rodrigoclira@yahoo.com.br)
from django.db import models
import datetime
from os import sep
from django.contrib.auth.models import User
from django.contrib.comments.moderation import CommentModerator, moderator
#from django.db.models import permalink

class Post (models.Model):
	title = models.CharField('título', max_length=100, unique=True)
	image = models.ImageField('imagem', upload_to='images'+ sep +'blog', blank=True)
	text = models.TextField("conteúdo")
	description = models.TextField("descrição")
	published = models.DateTimeField('Data de publicação', default=datetime.datetime.now, blank=False) #auto_now_add=True
	category = models.ForeignKey('blog.Category')
	author = models.ForeignKey(User)

	def was_published_recently(self):
		return self.published >= datetime.datetime.now() - datetime.timedelta(days=1)

	was_published_recently.admin_order_field = '-published'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Publicado recentemente?'

	def __unicode__(self):
		return ("%s" % self.title)

	class Meta:
		verbose_name = "postagem"
		verbose_name_plural = "postagens"
	
class Category(models.Model):
	name = models.CharField('nome', max_length=100, unique=True, db_index=True)

	def __unicode__(self):
		return ("%s" % self.name)

	class Meta:
		verbose_name = "categoria"
		verbose_name_plural = "categorias"

class Image(models.Model):
	image = models.ImageField('imagem',upload_to='images'+ sep +'blog') 
	description = models.CharField('Breve Descrição', max_length = 50)	
	upload_date = models.DateTimeField('Data de upload', default=datetime.datetime.now, blank=False)

class PostModerator(CommentModerator):
	email_notification = False
	auto_close_field = 'published'
	close_after = 7

moderator.register(Post, PostModerator)
