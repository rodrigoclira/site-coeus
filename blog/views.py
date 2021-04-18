# -*- coding: utf-8 -*-
#<Autor> Rodrigo Lira (rodrigoclira@yahoo.com.br)
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from blog.models import Post
from coeus.tools import get_year, lasts_months, get_month, has_solucao
from django.template import RequestContext

MAX_POST_PER_PAGE = 5

def posts_months():
	temp_months = lasts_months(get_month())
	months = []
	for m,y in temp_months:
		quantity = Post.objects.filter(published__year = y).filter(published__month = m).count()
		if quantity:
			months.append((m, y,quantity))
	return months

def recent_posts():
	return Post.objects.all().order_by('-published')[:5]

# Pegar uma pagina com MAXIMUM_POST_PER_PAGE
def posts_page(request, page_id):
	upper_limit = int(page_id) * MAX_POST_PER_PAGE
	lower_limit = upper_limit - MAX_POST_PER_PAGE
	all_posts = Post.objects.all()
	posts_list = all_posts[lower_limit:upper_limit]
	recents = recent_posts()
	year = get_year()
	posts_by_month = posts_months()
	solucao = has_solucao()

	if page_id == 1:
		previous_page = None
	else:
		previous_page = int(page_id) - 1

	next_page = int(page_id) + 1 if len(all_posts) > upper_limit else None
	
	#posts_list = sorted(posts_list,lambda x,y:cmp(y.id,x.id)) # bug da ordem
	posts_list = posts_list[::-1]

	return render_to_response("blog/index.html", {'posts': posts_list, 'year': year, 
	'recent_posts': recents,'post_months': posts_by_month, 'next_page': next_page, 
	'previous_page': previous_page, 'page_id': page_id, 'solucao': solucao })

def posts_author(request, author_id):
	post_list_filtered = Post.objects.filter(author__id = author_id)
	posts_by_month = posts_months()
	year = get_year()
	recents = recent_posts()
	solucao = has_solucao()

	return render_to_response('blog/index.html', {'posts': post_list_filtered, 
	'year': year, 'recent_posts': recents, 'post_months': posts_by_month, 'solucao': solucao}) 

def posts_year(request, year):
	post_list_filtered = Post.objects.filter(published__year = year)
	posts_by_month = posts_months()
	year = get_year()
	recents = recent_posts()
	solucao = has_solucao()
	return render_to_response('blog/index.html', {'posts': post_list_filtered, 
			'post_months': posts_by_month, 'year': year, 'recent_posts': recents, 
			'solucao': solucao }) 

def posts_month(request, year, month):
	post_list_filtered = Post.objects.filter(published__year = year).filter(published__month = month)
	posts_by_month = posts_months()
	year = get_year()
	recents = recent_posts()
	solucao = has_solucao()
	return render_to_response('blog/index.html', {'posts': post_list_filtered,
							'post_months': posts_by_month, 'year': year, 'recent_posts': recents, 
							'solucao': solucao }) 

def index(request):
	return redirect('/blog/posts/page/1', permanent=True)


def detail(request, post_id):
	p = get_object_or_404(Post, pk=post_id)
	year = get_year()
	recents = recent_posts()
	posts_by_month = posts_months()
	return render_to_response('blog/detail.html', {'post': p, 'year': year, 'recent_posts': recents, 'post_months': posts_by_month , 'next': '/blog/post/' + post_id },	context_instance = RequestContext(request))

def comment(request):
    # Redirecting after comment submission
    return HttpResponseRedirect(request.POST['next'])

