#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views import SurveyCreateView, SurveyDetailView, SurveyListView
from . import views


urlpatterns = patterns('',
    url(r'^results$', SurveyListView.as_view(), name='likert_list'),
    url(r'^$', SurveyCreateView.as_view(), name="likert_add"),
	url(r'^ncontemp$', views.NorConView.as_view(), name='northerncontemp'),
 	url(r'^noriginal$', views.NorOrigView.as_view(), name='northernoriginal'),
 	url(r'^soufried$', views.SoFried.as_view(), name='southernfried'),
    url(r'^added/$', TemplateView.as_view(template_name='likert/added.html'), name='likert_added'),
    # url(r'^toptracks/(?P<pk>\w+)/$', SurveyDetailView.as_view(), name='likert_detail'),

)



urlpatterns += staticfiles_urlpatterns()