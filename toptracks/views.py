from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader,Context
### BootStrap Modules
from django.views.generic.base import TemplateView

#
## Ratings Modules
import datetime

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'toptracks/base.html'


class NorConView(TemplateView):
    template_name = 'toptracks/northern_contemp.html'

class NorOrigView(TemplateView):
	template_name = 'toptracks/northern_original.html'

class SoFried(TemplateView):
	template_name = 'toptracks/southern_fried.html'