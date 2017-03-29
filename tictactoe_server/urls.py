from django.conf.urls import include, url
from tictactoe_server import views

from django.contrib import admin
admin.autodiscover()

#urlpatterns = patterns('',
urlpatterns = [
    # Examples:
    # url(r'^$', 'chat_server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^get_games/$', views.get_games, name='get_games'),
    url(r'^get_game/$', views.get_game, name='get_game'),
    url(r'^create_game/$', views.create_game, name='create_game'),
    url(r'^join_game/$', views.join_game, name='join_game'),
    url(r'^leave_game/$', views.leave_game, name='leave_game'),
    url(r'^take_spot/$', views.take_spot, name='take_spot'),

    # url(r'^admin/', include(admin.site.urls)),
    # url(r'chat/', include('chat.urls', namespace="chat")),
]
#)

