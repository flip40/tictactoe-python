from django.conf.urls import patterns, url
from chat import views

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'chat_server.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^$', views.chat, name='index'),
	url(r'^updatechat/$', views.update_chat, name='updatechat'),
	url(r'^sendmessage/$', views.send_message, name='sendmessage'),
)
