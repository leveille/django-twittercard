from django.conf.urls import patterns, url

from example.views import HomePageView, SubPageView

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^sub/$', SubPageView.as_view(), name='sub'),
)
