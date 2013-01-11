from django.conf.urls import patterns, url

from example.views import SummaryCardView, PhotoCardView

urlpatterns = patterns('',
    url(r'^$', SummaryCardView.as_view(), name='summary-card'),
    url(r'^photo-card/$', PhotoCardView.as_view(), name='photo-card'),
)
