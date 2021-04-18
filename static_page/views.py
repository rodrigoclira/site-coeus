#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from coeus.tools import get_year, has_solucao
from django.http import HttpResponse
	

def contato(request):
	solucao = has_solucao()
	return render_to_response('contato/index.html', { 'year' : get_year(), 'solucao': solucao})	

def error404(request):
	solucao = has_solucao()
	return render_to_response('404.html', { 'year' : get_year(), 'solucao': solucao})	

def error500(request):
	solucao = has_solucao()
	return render_to_response('500.html', { 'year' : get_year(), 'solucao': solucao})	
