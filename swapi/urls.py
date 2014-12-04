from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'$', 'swapi.views.index')
)
