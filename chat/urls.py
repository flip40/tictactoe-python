from django.conf.urls import patterns, url
from chat import views

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'chat_server.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^$', views.chat, name='index'),
)
