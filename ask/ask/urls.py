from django.conf.urls import patterns, include, url
from qa import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^login/', 'django.contrib.auth.views.login', {
        'template_name':'login.html'}, name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {
        'next_page':'/'}, name='logout'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^question/(?P<qid>\w+)/$', views.question_details, name='question-details'),
    url(r'^ask/', views.question_add, name='question-add'),
    url(r'^answer/', views.answer_question, name='answer-question'),
    url(r'^popular/', views.popular, name='popular'),
    url(r'^new/', views.test)
    #url(r'^admin/', include(admin.site.urls)),
)
