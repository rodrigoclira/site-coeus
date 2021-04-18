from django.conf.urls.defaults import *

urlpatterns = patterns('areas_de_atuacao.views',
	url(r'^(?P<area_id>\d+)/$','detail'),
	url(r'^$',"index"),
)

