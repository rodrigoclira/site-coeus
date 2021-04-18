from django.conf.urls.defaults import *
from blog.models import Post

urlpatterns = patterns('blog.views',
	url(r'^post/(?P<post_id>\d+)/$','detail'),
	url(r'^$',"index"),
	url(r'^posts/autor/(?P<author_id>\d+)/$','posts_author'),
	url(r'^posts/(?P<year>\d{4})/$','posts_year'),
	url(r'^posts/(?P<year>\d{4})/(?P<month>\d{1,2})/$','posts_month'),
	url(r'^posts/page/(?P<page_id>\d+)/$','posts_page'),
)

