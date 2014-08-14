from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from BrewAPI import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BrewAPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^brews/$', views.BrewList.as_view()),
    url(r'^brews/(?P<pk>[0-9]+)/$', views.BrewDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)