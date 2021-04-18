# -- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from solucoes.models import Solucao
from coeus.tools import get_year, has_solucao
from django.http import Http404 

def index(request):
	produtos_list = Solucao.objects.all()
	year = get_year()
	solucao = has_solucao()

	if not solucao:
		raise Http404 

	return render_to_response("solucoes/index.html", {'produtos': produtos_list, 'year': year, 
	'solucao': solucao})

def detail(request, solucao_id):
	p = get_object_or_404(Solucao, pk=solucao_id)
	produtos_list = Solucao.objects.all()
	year = get_year()
	solucao = has_solucao()
	print p
	if not solucao:
		raise Http404 

	return render_to_response('solucoes/detail.html', {'produto': p, 'year': year,
	'produtos': produtos_list, 'solucao': solucao })


