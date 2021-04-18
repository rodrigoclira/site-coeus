# -- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from quem_somos_nos.models import Person
from django.http import Http404
from sys import stderr
from coeus.settings import MEDIA_ROOT
from coeus.tools import get_real_name, get_year, has_solucao

def index(request):
	person_list = Person.objects.all()
	year = get_year()
	solucao = has_solucao()
	return render_to_response("quem-somos-nos/index.html", {'persons': person_list, 'year': year, 
	'solucao': solucao })


def detail(request, pessoa_id):
	realname = get_real_name(pessoa_id)
	year = get_year()
	person = get_object_or_404(Person,name=realname)
	solucao = has_solucao()
	return render_to_response('quem-somos-nos/detail.html', {'person':person,  
							'year':year	,"media": MEDIA_ROOT, 'solucao': solucao })

