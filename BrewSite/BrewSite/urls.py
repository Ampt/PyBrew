from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('BrewSite.views',
    # Examples:
    # url(r'^$', 'BrewSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^brews/$', 'brew_list'),
    url(r'^brews/(?P<pk>[0-9]+)/$', 'brew_detail'),
)
