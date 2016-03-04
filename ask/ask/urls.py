from django.conf.urls import patterns, include, url
from qa import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.test, name='home'),
    url(r'^login/', views.test, name='login'),
    url(r'^signup/', views.test, name='signup'),
    url(r'^question/(?P<qid>\w+)/$', views.test),
    url(r'^ask/', views.test, name='ask'),
    url(r'^popular/', views.test, name='popular'),
    url(r'^new/', views.test),

    #url(r'^admin/', include(admin.site.urls)),
)
