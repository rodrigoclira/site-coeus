#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.utils.encoding import force_unicode
from django.db import models
from solucoes.models import Solucao
from coeus.settings import NAO_TESTAR_SOLUCAO

get_year = lambda : datetime.now().year
get_month = lambda : datetime.now().month
has_solucao = lambda : NAO_TESTAR_SOLUCAO or (len(Solucao.objects.all()) != 0)

#months = ['','janeiro','fevereiro', u'mar\xe7o','abril','maio','junho','julho',
#		'agosto','setembro','outubro','novembro','dezembro']

get_real_name = lambda name : ' '.join(name.split('-')).title()

def lasts_months(current_month, quantity=6):
	lasts=[]
	for number in range(0, quantity):
		month = current_month - number
		year = get_year()
		if month < 1:
			month = month + 12
			year -= 1
		lasts.append([month, year])
	return lasts


