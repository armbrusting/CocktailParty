from django.conf.urls import patterns, url

from parties import views

urlpatterns = patterns('',
    # ex: /parties/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<party_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/cocktial/
    url(r'^(?P<party_id>\d+)/cocktails/$', views.cocktails, name='cocktails'),
    # ex: /polls/5/??/
    #url(r'^(?P<poll_id>\d+)/??/$', views.??, name='??'),
    )
