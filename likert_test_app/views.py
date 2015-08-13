#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
#from .forms import SurveyForm
from .models import ParametersModel
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
### BootStrap Modules
from django.views.generic.base import TemplateView
#
## Ratings Modules
import datetime


####### LikeRThizzle
class SurveyListView(ListView):
    context_object_name = 'surveys'
    model = ParametersModel
    template_name = 'likert/index.html'


class SurveyCreateView(CreateView):
    model = ParametersModel
    #fields = ['item', 'another_item']
    fields = [ 'question_1','question_2','question_3' ]
    #form_class = SurveyForm
    template_name = 'likert/add.html'
    success_url = reverse_lazy('likert_added')


class SurveyDetailView(DetailView):
    context_object_name = 'survey'
    model = ParametersModel
    template_name = 'likert/detail.html'


# Create your views here.

class HomePageView(CreateView):
    context_object_name = 'surveys'
    model = ParametersModel
    fields = [ 'question_1','question_2','question_3' ]
    template_name = 'likert/add.html'
    success_url = reverse_lazy('likert_added')


class NorConView(CreateView):
    context_object_name = 'surveys'
    model = ParametersModel
    fields = [ 'question_1','question_2','question_3' ]
    template_name = 'likert/ncontemp.html'
    success_url = reverse_lazy('likert_added')

class NorOrigView(CreateView):
    context_object_name = 'surveys'
    model = ParametersModel
    fields = [ 'question_1','question_2','question_3' ]
    template_name = 'likert/noriginal.html'
    success_url = reverse_lazy('likert_added')

class SoFried(CreateView):
    context_object_name = 'surveys'
    model = ParametersModel
    fields = [ 'question_1','question_2','question_3' ]
    template_name = 'likert/sofried.html'
    success_url = reverse_lazy('likert_added')




    