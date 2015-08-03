from django.conf.urls import url
from toptracks.views import HomePageView
from . import views

urlpatterns = [
    # url(r'^$', views.home, name='home'),
 	url(r'^$', HomePageView.as_view(), name='home'),
 	url(r'^ncontemp$', views.NorConView.as_view(), name='northerncontemp'),
 	url(r'^noriginal$', views.NorOrigView.as_view(), name='northernoriginal'),
 	url(r'^soufried$',views.SoFried.as_view(), name='southernfried'),
]
