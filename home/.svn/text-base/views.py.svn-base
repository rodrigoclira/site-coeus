# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from coeus.tools import get_year, has_solucao
from home.models import Slide, Slider

HOME_ID = Slider.objects.filter(name="home")[0].id

def home(request):
	slides = Slide.objects.filter(slider=HOME_ID)
	solucao = has_solucao()
	return render_to_response('home/index.html', { 'year' : get_year(), 
	'slides': slides, 'solucao': solucao })

