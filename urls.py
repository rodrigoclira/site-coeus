from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'static_page.views.error404'
handler500 = 'static_page.views.error500'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coeus.views.home', name='home'),
    # url(r'^coeus/', include('coeus.foo.urls')),
	url(r'^$', 'home.views.home'),
	url(r'^index/$','home.views.home'),
	url(r'^home/$','home.views.home'),
	url(r'^contato/$','static_page.views.contato'),
#	url(r'^comments/post/$','views.comments.post_comment',name='comments-post-comment'),

	url(r'^quem-somos/',include('quem_somos_nos.urls')),
	url(r'^blog/',include('blog.urls')),
	url(r'^areas-de-atuacao/',include('areas_de_atuacao.urls')),
	url(r'^solucoes/',include('solucoes.urls')),
    url(r'^coeus/admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
#	url(r'^comments/posted/$','blog.views.comment_posted'),
	url(r'^comments/', include('django.contrib.comments.urls')),
)
