from django.conf.urls import patterns, include, url
from main_site import views
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SamTweb.views.home', name='home'),
    # url(r'^SamTweb/', include('SamTweb.foo.urls')),

    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),

	url(r'^index/(?P<i>\d+)/', views.serve_index_page, name = 'serve_index_page'),
    url(r'^index/', views.serve_index, name = 'serve_index'),
    url(r'^share/', views.serve_share, name = 'serve_share'),
    url(r'^submitme_thanks/',views.serve_submitme_thanks, name = 'serve_submitme_thanks'),
    url(r'^$', views.serve_index, name = 'serve_index'),
)
urlpatterns += patterns('',
        (r'^main_site/static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    )