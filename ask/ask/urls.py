from django.conf.urls import patterns, include, url
from qa import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.test, name='home'),
    url(r'^login/', 'django.views.defaults.page_not_found', name='login'),
    url(r'^signup/', 'django.views.defaults.page_not_found', name='signup'),
    url(r'^question/(?P<qid>\w+)/$', views.test),
    url(r'^ask/', 'django.views.defaults.page_not_found', name='ask'),
    url(r'^popular/', 'django.views.defaults.page_not_found', name='popular'),
    url(r'^new/', 'django.views.defaults.page_not_found'),

    #url(r'^admin/', include(admin.site.urls)),
)
