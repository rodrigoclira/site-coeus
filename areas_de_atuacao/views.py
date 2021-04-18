# -- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from areas_de_atuacao.models import Area
from coeus.tools import get_year, has_solucao

def index(request):
	areas_de_atuacao_list = Area.objects.all()
	servicos_list = []
	year = get_year()
	solucao = has_solucao()
	return render_to_response("areas-de-atuacao/index.html", {'areas': areas_de_atuacao_list, 
	'servicos': servicos_list, 'year': year, 'solucao': solucao })

def detail(request, area_id):
	p = get_object_or_404(Area, pk=area_id)
	year = get_year()
	solucao = has_solucao()
	return render_to_response('areas-de-atuacao/detail.html', {'area_id': p, 
	'year': year, 'solucao': solucao })


