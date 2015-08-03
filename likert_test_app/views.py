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
##### Template System
from django.template.loader import get_template
####### LikeRThizzle
# Jacked Views
# 
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
# 
# Custum Views
#
class HomePageView(CreateView):
    context_object_name = 'surveys'
    model = ParametersModel
    fields = [ 'question_1','question_2','question_3' ]
    template_name = 'likert/add.html' 
    success_url = reverse_lazy('likert_added')
    video_url = 'http://www.youtube.com/embed/Cvu0Q4Cl7pU'
    video_id = 'Cvu0Q4Cl7pU'


    def get_context_data(self, **kwargs):
        template = loader.get_template(self.template_name)
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['video'] = self.video_url
        return context


    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(HomePageView, self).form_valid(form)
        
        

class NorConView(CreateView):
    context_object_name = 'surveys'
    model = ParametersModel
    fields = [ 'question_1','question_2','question_3' ]
    template_name = 'likert/ncontemp.html'
    # Inner class Funcionality and Variables
    success_url = reverse_lazy('likert_added')



class NorOrigView(CreateView):
    context_object_name = 'surveys'
    model = ParametersModel
    fields = [ 'question_1','question_2','question_3' ]
    template_name = 'likert/noriginal.html'
     # Inner class Funcionality and Variables
    success_url = reverse_lazy('likert_added')

class SoFried(CreateView):
    context_object_name = 'surveys'
    model = ParametersModel
    fields = [ 'question_1','question_2','question_3' ]
    template_name = 'likert/sofried.html'
     # Inner class Funcionality and Variables
    success_url = reverse_lazy('likert_added')








    