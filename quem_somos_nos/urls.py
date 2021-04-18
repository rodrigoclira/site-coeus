from django.conf.urls.defaults import *

urlpatterns = patterns('quem_somos_nos.views',
	url(r'^(?P<pessoa_id>\w+\-?\w+\-?\w+)/$','detail'),
#	url(r'^(?P<pessoa_id>\w+\-?\w+?\-\w+)/$','detail'),
	url(r'^$',"index"),
)

