from django.conf.urls import url
from .views import RssLinksView, RssLinksUpdateView, RssLinksCreateView

urlpatterns = [
    url(r'^$', RssLinksView.as_view()),
    url(r'^create/$', RssLinksCreateView.as_view()),
    url(r'update/(?P<id>\d+)$', RssLinksUpdateView.as_view()),
]
