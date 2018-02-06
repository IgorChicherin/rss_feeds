from django.conf.urls import url
from .views import RssLinksView, RssLinksUpdateView, RssLinksCreateView, RssLinksDeleteView

urlpatterns = [
    url(r'^$', RssLinksView.as_view()),
    url(r'^create/$', RssLinksCreateView.as_view()),
    url(r'^update/(?P<pk>\d+)$', RssLinksUpdateView.as_view()),
    url(r'^delete/(?P<pk>\d+)$', RssLinksDeleteView.as_view()),
]
