from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^newgame/$', views.new_game, name='newgame'),
	url(r'^game/(?P<short_id>\w{4})$', views.game, name='game'),
]