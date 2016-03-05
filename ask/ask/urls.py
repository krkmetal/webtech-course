from django.conf.urls import patterns, include, url
from qa import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^login/', views.test, name='login'),
    url(r'^signup/', views.test, name='signup'),
    url(r'^question/(?P<qid>\w+)/$', views.question_details, name='question-details'),
    url(r'^ask/', views.test, name='ask'),
    url(r'^popular/', views.popular, name='popular'),
    url(r'^new/', views.test),

    #url(r'^admin/', include(admin.site.urls)),
)
